from __future__ import unicode_literals
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os
from email.mime.image import MIMEImage
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def email_client(self, subject, text):
    # Send the client an email
    html_content = render_to_string("../templates/baseTemplates/emailToUser.html", {'salutation': self.salutation,
                                                                                    'last_name': self.last_name,
                                                                                    'text_body': text})
    msg = EmailMultiAlternatives(subject, 'Dear ' + self.salutation + ' ' +
                                 self.last_name + '/n' + text,
                                 'diss@asranet.co.uk', [self.email], )
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('static/Images/asranetLogo.jpg')
    msg.mixed_subtype = 'related'

    f = 'asranetLogo.jpg'
    fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
    msg_img = MIMEImage(fp.read())
    fp.close()
    msg_img.add_header('Content-ID', '<{}>'.format(f))
    msg.attach(msg_img)
    msg.send()


def email_admin(self, subject, text, sorted_self):

    styleSheet = getSampleStyleSheet()

    # Send the admin a PDF of client details
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clientDetails.pdf"'

    string_buffer = StringIO()

    new_pdf = []
    header = Paragraph("DISS Attendee Details", styleSheet['Heading1'])
    new_pdf.append(header)

    for element in sorted_self:
        new_pdf.append(Paragraph(element[0], styleSheet['Heading3']))
        new_pdf.append(Paragraph(element[1], styleSheet['BodyText']))
        new_pdf.append(Spacer(1, 2))

    doc = SimpleDocTemplate(string_buffer)
    doc.build(new_pdf)
    pdf = string_buffer.getvalue()
    string_buffer.close()

    msg = EmailMultiAlternatives(subject, text, "diss@asranet.co.uk", ["blair.calderwood@asranet.co.uk"])
    msg.attach(self.first_name + self.last_name + "DISS.pdf", pdf, "application/pdf")
    msg.send()
