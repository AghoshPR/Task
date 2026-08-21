
# models
# ----------------------------------------------

class DeliveryDate(models.Model):

    orderdate = models.DateField()
    select_place = models.charField(15)
    delivery_date = models.IntegerField()

# ----------------------------------------------


from django.utils import timezone
from django.view import View

class ShippingDate(View):

    def post(self,request):

        orderdate = timezone.now()

        select_place = request.data.get('place')

        delivery_date=0

        month={
                    january:31
                    february:28
                    march:31
                    april:30
                    may:31
                    june:30
                    july:31
                    august:31
                    september:30
                    october:31
                    noveber:30
                    december:31
        }

        if select_place =='UAE':

            exact_month = orderdate.strftime()

            for k,v in month.items():

                if k==exact_month:

                    delivery_date = v - 6
   

        elif select_place =='DEFAULT':

            exact_month = orderdate.strftime()
            
            for k,v in month.items():

                if k==exact_month:

                    delivery_date = v - 6

        product_deliver_date = delivery_date - orderdate

        context={
            'product_deliver_date':product_deliver_date
        }

        return render(request,'delivery.page.html',context)
        
                  
            
            
