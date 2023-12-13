# # from core import settings
# from django_xhtml2pdf.utils import generate_pdf
# from django.http import HttpResponse, HttpResponseServerError
# from django.template import RequestContext
# from django.template.loader import get_template
# from io import BytesIO
# from unittest import loader
# from xhtml2pdf import pisa
# import django.http
# import os
# # from core import settings

# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.contrib.staticfiles import finders
# from django.views.generic import View 

# # class GerarPDF():
# #     def render_to_pdf(self, template_end, context_dict={}):
# #         template = get_template(template_end)
# #         html = template.render(context_dict)
# #         result = BytesIO()
# #         try:
# #             pdf = pisa.pisaDocument(BytesIO(html.encode("")), result)
# #             return django.http.HttpResponse(result.getvalue(),
# #                                 content_type = 'application/pdf')
# #         except Exception as erroPdf:
# #             print(erroPdf)
# #             return None
        

# # class GerarPDF():
# #     def render_to_pdf(self, template_end, context_dict={}):
# #         template = get_template(template_end)
# #         html = template.render(context_dict)
# #         result = BytesIO()
# #         try:
# #             pdf = pisa.pisaDocument(BytesIO(html.encode("")), result)
# #             response = HttpResponse(content_type='application/pdf')
# #             response['Content-Disposition'] = f'filename="{template_end}.pdf"'
# #             response.write(result.getvalue())
# #             return response
# #         except Exception as erroPdf:
# #             print(erroPdf)
# #             return HttpResponseServerError("Erro ao gerar o PDF")

# # class GerarPDF():
# #     def render_to_pdf(self, template_path, context_dict={}):
# #         template = loader.get_template(template_path)
# #         context = RequestContext(self.request, context_dict)
# #         html = template.render(context)
# #         result = BytesIO()
# #         try:
# #             pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
# #             if not pdf.err:
# #                 response = HttpResponse(result.getvalue(), content_type='application/pdf')
# #                 response['Content-Disposition'] = f'filename="{template_path}.pdf"'
# #                 return response
# #         except Exception as erroPdf:
# #             print(erroPdf)
# #         return HttpResponseServerError("Erro ao gerar o PDF")
    




# # class PDFGenerator:
# #     def render_to_pdf(self, template_name, context_dict={}):
# #         template = get_template(template_name)
# #         html = template.render(context_dict)
# #         result = BytesIO()

# #         try:
# #             pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
# #             if not pdf.err:
# #                 response = HttpResponse(content_type='application/pdf')
# #                 response['Content-Disposition'] = f'attachment; filename="certificado.pdf"'
# #                 response.write(result.getvalue())
# #                 return response
# #         except Exception as e:
# #             print(str(e))
# #             return None

# # class PDFGenerator:
# #     def render_to_pdf(self, template_name, context_dict={}):
# #         template = get_template(template_name)
# #         html = template.render(context_dict)
# #         result = BytesIO()

# #         try:
# #             pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding="UTF-8", link_callback=None, show_error_as_pdf=True)
# #             if not pdf.err:
# #                 response = HttpResponse(content_type='application/pdf')
# #                 response['Content-Disposition'] = f'attachment; filename="certificado.pdf"'
# #                 response.write(result.getvalue())
# #                 return response
# #         except Exception as e:
# #             print(str(e))
# #             return None

# # class PDFGenerator:
# #     def render_to_pdf(self, template_name, context_dict={}):
# #         template = get_template(template_name)
# #         html = template.render(context_dict)
# #         result = BytesIO()

# #         def link_callback(uri, rel):
# #             # Use o link_callback para converter URLs absolutas para caminhos locais
# #             if uri.startswith(settings.STATIC_URL):
# #                 uri = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
# #             elif uri.startswith(settings.MEDIA_URL):
# #                 uri = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
# #             return uri

# #         try:
# #             pdf = pisa.pisaDocument(
# #                 BytesIO(html.encode("UTF-8")),
# #                 result,
# #                 encoding="UTF-8",
# #                 link_callback=link_callback,
# #                 show_error_as_pdf=True
# #             )
# #             if not pdf.err:
# #                 response = HttpResponse(content_type='application/pdf')
# #                 response['Content-Disposition'] = f'attachment; filename="certificado.pdf"'
# #                 response.write(result.getvalue())
# #                 return response
# #         except Exception as e:
# #             print(str(e))
# #             return None



# # def myview(response):
# #     resp = HttpResponse(content_type='application/pdf')
# #     result = generate_pdf('my_template.html', file_object=resp)
# #     return result




# # def myview(response):
# #     resp = HttpResponse(content_type='application/pdf')
# #     result = generate_pdf('certificado/base_cert.html', file_object=resp)
# #     return result

# # SOURCE = "<html><body><p>PDF from string</p></body></html>"

# # OUTPUT_FILENAME = "test.pdf"

# # def html_to_pdf(content, output):
# #     """
# #     Generate a pdf using a string content

# #     Parameters
# #     ----------
# #     content : str
# #         content to write in the pdf file
# #     output  : str
# #         name of the file to create
# #     """
# #     # Open file to write
# #     result_file = open(output, "w+b") # w+b to write in binary mode.

# #     # convert HTML to PDF
# #     pisa_status = pisa.CreatePDF(
# #             content,                   # the HTML to convert
# #             dest=result_file           # file handle to recieve result
# #     )           

# #     # close output file
# #     result_file.close()

# #     result = pisa_status.err

# #     if not result:
# #         print("Successfully created PDF")
# #     else:
# #         print("Error: unable to create the PDF")    

# #     # return False on success and True on errors
# #     return result

# # def from_text(source, output):
# #     """
# #     Generate a pdf from a plain string

# #     Parameters
# #     ----------
# #     source : str
# #         content to write in the pdf file
# #     output  : str
# #         name of the file to create
# #     """
# #     html_to_pdf(source, output)



# # Define your data
# source_html = "<html><body><p>To PDF or not to PDF</p></body></html>"
# output_filename = "test.pdf"

# # Utility function
# def convert_html_to_pdf(source_html, output_filename):
#     # open output file for writing (truncated binary)
#     result_file = open(output_filename, "w+b")

#     # convert HTML to PDF
#     pisa_status = pisa.CreatePDF(
#             source_html,                # the HTML to convert
#             dest=result_file)           # file handle to recieve result

#     # close output file
#     result_file.close()                 # close output file

#     # return False on success and True on errors
#     return pisa_status.err

# # Main program
# if __name__ == "__main__":
#     pisa.showLogging()
#     convert_html_to_pdf(source_html, output_filename)

# def link_callback(uri, rel):
#             """
#             Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#             resources
#             """
#             result = finders.find(uri)
#             if result:
#                     if not isinstance(result, (list, tuple)):
#                             result = [result]
#                     result = list(os.path.realpath(path) for path in result)
#                     path=result[0]
#             else:
#                     sUrl = settings.STATIC_URL        # Typically /static/
#                     sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
#                     mUrl = settings.MEDIA_URL         # Typically /media/
#                     mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

#                     if uri.startswith(mUrl):
#                             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#                     elif uri.startswith(sUrl):
#                             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#                     else:
#                             return uri

#             # make sure that file exists
#             if not os.path.isfile(path):
#                     raise Exception(
#                             'media URI must start with %s or %s' % (sUrl, mUrl)
#                     )
#             return path

# def render_pdf_view(request):
#     template_path = 'user_printer.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#        html, dest=response, link_callback=link_callback)
#     # if error then show some funny view
#     if pisa_status.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# class PdfView(View):
#        def get(self, request, *args, **)

# encoding: utf-8

from django.template import Context, Template


def extract_request_variables(request):

    page_size = request.POST.get('page_size', 'letter')
    page_orientation = request.POST.get('page_orientation', 'portrait')

    pagesize = "%s %s" % (
        page_size, page_orientation
    )

    template = Template(request.POST.get('data', ''))
    data = template.render(Context({}))
    return {
        'pagesize': pagesize,
        'data': data,
        'page_orientation': page_orientation,
        'page_size': page_size,
        'example_number': request.POST.get("example_number", '1'),
        'border': request.POST.get('border', '')
    }