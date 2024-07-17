
from ..models import West_Info



# Recycling count

def countRcycling():
    recycling_records = West_Info.objects.filter(Prediction="RECYCLING").count()
    
    return recycling_records


# non recycling count  



def countNonRcycling():
    NonRecycling_records = West_Info.objects.filter(Prediction="NON RECYCLING").count()
    
    return NonRecycling_records
    
    
    

                
                
def filter_ws(request):
    if request.method == 'POST':
        # classes =  {0:'cardboard', 1:'glass', 2:'metal', 3:'paper', 4:'plastic'}
        if request.POST.get('select_ws') == "plastic":
            plastic = West_Info.objects.filter(Type = "plastic").values()
            return  plastic
        
        elif request.POST.get('select_ws') == "paper":
            paper = West_Info.objects.filter(Type = "paper").values()
            return paper
        
        elif request.POST.get('select_ws') == "metal":
            metal = West_Info.objects.filter(Type = "metal").values()
            return metal
        
        elif request.POST.get('select_ws') == "glass":
            glass = West_Info.objects.filter(Type = "glass").values()
            return glass
        
        elif request.POST.get('select_ws') == "cardboard":
            cardboard = West_Info.objects.filter(Type = "cardboard").values()
            return cardboard
        else :
            All_ws = West_Info.objects.all()
            return All_ws
    else:  
        
        All_ws = West_Info.objects.all()
        return All_ws