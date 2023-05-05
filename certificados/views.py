from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Generar PDF
def pdfgenerator(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text
    lines = [
        "Hola",
        "Mundo",
        "XD",
    ]

    # Loop
    for line in lines:
        textob.textLine(line)

    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return
    return FileResponse(buf, as_attachment=True, filename='prueba.pdf')


# Create your views here.

def login_view(request):
    return render(request,"certificados/login.html")

@login_required
def dash_view(request):
    return render(request,"certificados/dashboard.html")





