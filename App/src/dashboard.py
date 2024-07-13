
from ..models import West_Info



# Recycling count

def countRcycling():
    recycling_records = West_Info.objects.filter(Prediction="RECYCLING").count()
    
    return recycling_records


# non recycling count  



def countNonRcycling():
    NonRecycling_records = West_Info.objects.filter(Prediction="NON RECYCLING").count()
    
    return NonRecycling_records
    
    
    

                
                
def top_five():
    records = West_Info.objects.all()[:5]
    
    return records