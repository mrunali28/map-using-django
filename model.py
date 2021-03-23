
class Order(models.Model):
   
    order_id = models.CharField(max_length=250, null=True, blank=True)
    product_details = models.ForeignKey(ProductDetails, on_delete=models.CASCADE, related_name="product_details_order",
                                        null=True, blank=True)
   
    unique_order_id = models.CharField(max_length=250, null=True, blank=True, db_index=True)
    
    def __str__(self):
        return '%s %s' % (self.order_id, self.unique_order_id)





class OrderDetails(models.Model):
    
    order_text = models.CharField(max_length=100, null=True, blank=True)
   
  
    total_amount = models.FloatField(default=0, null=True, blank=True, db_index=True)
    date = models.DateTimeField(null=True, blank=True, db_index=True)
    re_status = models.BooleanField(default=True, db_index=True)
    status = models.CharField(max_length=256, null=True, blank=True, choices=ecom_constants.ORDER_STATUS, db_index=True)
   
    order_id = models.ManyToManyField(Order, related_name="oderdetails_order", null=True,
                                      blank=True)
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_user", blank=True, null=True)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="orderdertails_addr", null=True,
                                blank=True)
   
