import os
import pdfkit
arr = os.listdir('V:/Final_Project/DBA')

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
add_name = 'V:/Final_Project/DBA/'
sub_name = 'V:/Final_Project/Resume_fin/'
for i in arr:
    j = add_name + i
    f = sub_name + i[:-5]+'.pdf'
    try:
        pdfkit.from_file(j, f,configuration=config)
    except:
        pass
    finally:
        print(i)
