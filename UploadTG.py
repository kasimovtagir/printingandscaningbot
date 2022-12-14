from email import message
from telebot import types
import telebot
import os
import subprocess
from PIL import Image
#\from telegram import ReplyMarkup
from PyPDF2 import PdfFileReader

file_name=""
file_rename=""
save_dir=""
file_extension = ""

import CallBackTG
#os.system("mkdir /mnt/File/")

def convert_to(doc_path, path):
    subprocess.call(['soffice',
                             # '--headless',
                             '--convert-to',
                             'pdf',
                             '--outdir',
                             path,
                             doc_path])
    #print(doc_path)                        
    return doc_path

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
 
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.show()
    resized_image.save(output_image_path)

def rename_file_name (bot, path, file, message):
    global file_extension
    file_rename = (file.replace(" ", "-"))
    file_rename = (file_rename.replace("(", "-"))
    file_rename = (file_rename.replace(")", "-"))

    os.rename(path + "/" +file, path + "/" +file_rename)

    split_tup = os.path.splitext(file_rename)

    file_extension = split_tup[1]

    data = bot.current_states.get_data(message.chat.id, message.chat.id )
    if data is not None:
        choose_printer = data.get("choose_printer")

    else:
        choose_printer = None

    if str(file_extension) in [".doc", ".docx", ".odt"]:
        convert_to(path + "/"+file_rename, path)
        convert_name = split_tup[0]+".pdf"
        bot.current_states.set_data(message.chat.id, message.from_user.id, "file_name", convert_name)

        with open(path + "/" +convert_name, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()



        bot.send_message(message.chat.id,"?????? ??????????: - "+ format(str(convert_name))+"\n??????????????: - "+ str(choose_printer), reply_markup=CallBackTG.pre_printing())
        #return convert_name

    elif str(file_extension) in  [".jpg", ".png", ".jpeg"]:
        file_size = os.path.getsize(path + "/"+file_rename)
        if file_size >=2000000:
            resize_image(input_image_path=path + "/"+file_rename,
                output_image_path=path +"/Resize_"+file_rename ,
                size=(1920, 1080))
            #CallBackTG.file_name="Resize_"+file_rename
            f_n="/Resize_"+ file_rename
            file_rename = path +"/Resize_"+file_rename
            bot.current_states.set_data(message.chat.id, message.from_user.id, "file_name", f_n)

            print(file_rename)

            bot.send_message(message.chat.id,"?????? ??????????: - "+ f_n+"\n??????????????: - "+ str(choose_printer), reply_markup=CallBackTG.pre_printing())
        else: 
            #CallBackTG.file_name=file_rename
            if choose_printer =="":
                 CallBackTG.callback_list_Print(bot,message)
            else:     
                #CallBackTG.file_name=file_rename
                bot.send_message(message.chat.id,"?????? ??????????: - "+ file_rename +"\n??????????????: - "+ str(choose_printer), reply_markup=CallBackTG.pre_printing())
    
    elif str(file_extension) == ".pdf": 
        #CallBackTG.file_name=file_rename
        bot.current_states.set_data(message.chat.id, message.from_user.id, "file_name", file_rename)
        
        with open(path + "/" +file_rename, 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

       # CallBackTG.count_pages= number_of_pages        
        #= number_of_pages
        #bot.current_states.set_data(message.chat.id, message.from_user.id, "pages_print",pages_print)
        #print(pages_print)
        if choose_printer is None:
            CallBackTG.callback_list_Print(bot,message)
            #bot.send_message(message.chat.id,"???????????? ?????????????? ")
        else:
            bot.send_message(message.chat.id,"?????? ??????????: - "+ format(str(file_rename))+"\n??????????????: - "+ str(choose_printer), reply_markup=CallBackTG.pre_printing())

    else :
        bot.send_message(message.chat.id,"???????????? ?????????? ???? ????????????????????????????\n?????? ???????????????????????? ?????????? ?????????????? pdf, doc, docx, odt, jpg, jpeg, png.\n?????????? ???? ???????????? START")
        print(f"???????? {file_rename} ????????????")
        os.remove(path + "/"+file_rename)




def Upload_files(bot:telebot.TeleBot,message:telebot.types.Message):
    try:
        try:
            save_dir = "/mnt/File"
            # save_dir = message.caption
        except:
            save_dir = "/File"
            # save_dir = os.getcwd()
            s = "[!] you aren't entered directory, saving to {}".format(save_dir)
            bot.send_message(message.chat.id, str(s))
        file_name = message.document.file_name

        file_id = message.document.file_name
        file_id_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_id_info.file_path)
        print(f"???????????????????????? {str(message.from_user.first_name)} ???????????????? ????????: {str(file_name)}" )
        
        with open('logs.txt', 'a') as logs:
            logs.write( f"{str(CallBackTG.return_time())} - ????????????????????????: {str(message.from_user.first_name)} - ???????????????? ????????: {str(file_name)}\n")



        with open(save_dir + "/" + file_name, 'wb') as new_file:
                new_file.write(downloaded_file)
        try :
            bot.current_states.set_data(message.chat.id, message.from_user.id, "file_name", file_name)
        except:
            bot.current_states.set_state(message.chat.id, message.from_user.id, None)
            bot.current_states.reset_data(message.chat.id, message.chat.id)
            bot.current_states.set_data(message.chat.id, message.from_user.id, "file_name", file_name)
        rename_file_name(bot, save_dir, file_name, message)


        # os.remove(tagir)
    except Exception as ex:
        bot.send_message(message.chat.id, f"{ex}?????????????????????? ????????????\n?????????? ???? ???????????? START")