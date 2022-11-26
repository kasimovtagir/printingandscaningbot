
FROM debian:testing


# Install Packages (basic tools, cups, basic drivers, HP drivers)
RUN apt-get update \
&& apt-get install -y \
  sudo \
  whois \
  usbutils \
  cups \
  cups-client \
  cups-bsd \
  cups-filters \
  foomatic-db-compressed-ppds \
  printer-driver-all \
  openprinting-ppds \
  hpijs-ppds \
  hp-ppd \
  hplip \
  smbclient \
  printer-driver-cups-pdf \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Add user and disable sudo password checking
RUN useradd \
  --groups=sudo,lp,lpadmin \
  --create-home \
  --home-dir=/home/print \
  --shell=/bin/bash \
  --password=$(mkpasswd print) \
  print \
&& sed -i '/%sudo[[:space:]]/ s/ALL[[:space:]]*$/NOPASSWD:ALL/' /etc/sudoers

RUN apt update -y
RUN apt install mc -y
RUN apt install pip -y 
RUN apt install -y libreoffice-writer
RUN apt install -y nfs-common

COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the default configuration file
COPY --chown=root:lp cupsd.conf /etc/cups/cupsd.conf
#COPY --chown=root:lp printers.conf /etc/cups/printers.conf

RUN mkdir  /mnt/Scan
RUN mkdir  /mnt/Logs
RUN mkdir  /mnt/File



CMD ["--chown=root:lp /etc/cups/ppd/ -R"]


# Default shell
CMD ["/usr/sbin/cupsd", "-f"]

CMD [ "python3", "Main.py"]
RUN service cups restart
