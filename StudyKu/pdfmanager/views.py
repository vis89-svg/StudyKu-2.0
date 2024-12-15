from django.shortcuts import render, redirect
from .models import PDFDocument
from .forms import PDFUploadForm
from django.http import JsonResponse
# Upload view
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_pdf')
    else:
        form = PDFUploadForm()
    return render(request, 'pdfmanager/upload_pdf.html', {'form': form})

# Search view
def search_pdfs(request):
    query = request.GET.get('q', '')
    results = []
    suggestions = []
    pdf_urls = {}

    if query:
        results = PDFDocument.objects.filter(name__icontains=query)
        suggestions = PDFDocument.objects.filter(name__icontains=query).values_list('name', flat=True)

        # Create a mapping of PDF names to URLs
        for pdf in results:
            pdf_urls[pdf.name] = pdf.file.url

        # If it's an AJAX request, return suggestions
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'suggestions': list(suggestions), 'pdfUrls': pdf_urls})

    return render(request, 'pdfmanager/search_pdfs.html', {'results': results, 'query': query})

