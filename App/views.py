# predictor/views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
# from .forms import ImageUploadForm
from .src.utils import predict_image
from .models import West_Info


from .src.dashboard import countRcycling,countNonRcycling,top_five


# pridicting
@login_required(login_url='/login')
def image_upload_view(request):
    if request.method == 'POST':
        Image = request.FILES['uploadImage']
        # form = ImageUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     image = form.cleaned_data['image']
        fs = FileSystemStorage()
        img_path = fs.save(Image.name, Image)
        # img_url = fs.url(img_path)
        
        # Predict the image
        prediction = predict_image(fs.path(img_path))
        types = ""
        pr = ""
        PredictionText = ""
        classes =  {0:'cardboard', 1:'glass', 2:'metal', 3:'paper', 4:'plastic'}
        if prediction == 4:
            
            PredictionText = "Type = "+ classes[prediction] +" "+ " RECYCLING"
            types = classes[prediction]
            pr = "RECYCLING"

        else:
        
            PredictionText = "Type = "+ classes[prediction] +" "+ "NON RECYCLING"
            pr = "NON RECYCLING"
            types = classes[prediction]
            
        west = West_Info(
            Image_Path = img_path,
            Prediction = pr,
            Type = types
        
    )
        west.save()
        img_url = '/media/'+img_path
        return render(request, 'App/Predict.html', {
            'img_url': img_url,
            'prediction':  PredictionText,
            
        })
    else:
        return render(request, 'App/Predict.html')
    
    
    
    



# dashoard
@login_required(login_url='/login')
def dashboard(request):
    count_ws =  West_Info.objects.count()
    
    #  Pass the count to the template
 
    return render(request, 'App/Dashboard.html', {
        'recycling_count': countRcycling,
        'NonRcycling_count': countNonRcycling,
        "total": count_ws,
        "top_five":top_five
        
        })
    
    # total of count ws 
    

