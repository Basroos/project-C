from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.

CHOICES = (
    ("artichoke","artichoke"), 
    ("aubergine","aubergine"),
    ("asparagus","asparagus"),
    ("broccoflower","broccoflower"),
    ("broccoli","broccoli"),
    ("brussels sprouts","brussels sprouts"),
    ("cabbage","cabbage"),
    ("cauliflower","cauliflower"),
    ("celery","celery"),
    ("endive","endive"),
    ("bok choy","bok choy"),
    ("kale","kale"),("mustard greens","mustard greens"),("spinach","spinach"),("lettuce","lettuce"),("arugula","arugula"),("mushrooms","mushrooms"),("radicchio","radicchio"),("rhubarb","rhubarb"),("corn","corn"),("topinambur","topinambur"),("tat soi","tat soi"),("tomato","tomato"),
    ("alfalfa","alfalfa"),("azuki beans","azuki beans"),("black beans","black beans"),("bean sprouts","bean sprouts"),("black-eyed peas","black-eyed peas"),("green beans","green beans"),("kidney beans","kidney beans"),("lentils","lentils"),("peanuts","peanuts"),("soy beans","soy beans"),("peas","peas"),
    ("anise","anise"),("basil","basil"),("caraway","caraway"),("coriander","coriander"),("chamomile","chamomile"),("dill","dill"),("fennel","fennel"),("lavender","lavender"),("Cymbopogon","Cymbopogon"),("marjoram","marjoram"),("oregano","oregano"),("parsley","parsley"),("rosemary","rosemary"),("sage","sage"),("thyme","thyme"),
    ("Chives","Chives"),("Garlic","Garlic"),("Leek","Leek"),("onion","onion"),("shallot","shallot"),("scallion","scallion"),
    ("bell pepper","bell pepper"),("Jalapeño","Jalapeño"),("Habanero","Habanero"),("Paprika","Paprika"),("Tabasco pepper","Tabasco pepper"),("Cayenne pepper","Cayenne pepper"),
    ("beetroot","beetroot"),("carrot","carrot"),("celeriac","celeriac"),("corms","corms"),("ginger","ginger"),("parsnip","parsnip"),("rutabaga","rutabaga"),("radish","radish"),("wasabi","wasabi"),("potato","potato"),("sweet potato","sweet potato"),("yam","yam"),("turnip","turnip"),
    ("Açaí","Açaí"),("Akee","Akee"),("Apple","Apple"),("Apricot","Apricot"),("Avocado","Avocado"),("Banana","Banana"),("Blackberry","Blackberry"),("Blackcurrant","Blackcurrant"),("Blueberry","Blueberry"),("Crab apple","Crab apple"),("Cherry","Cherry"),("Coconut","Coconut"),("Cranberry","Cranberry"),("Date","Date"),("Dragonfruit","Dragonfruit"),("Grape","Grape"),
    ("Grapefruit","Grapefruit"),("Guava","Guava"),("Kiwifruit","Kiwifruit"),("Lemon","Lemon"),("Lime","Lime"),("Lychee","Lychee"),("Mango","Mango"),("Cataloupe Melon","Cataloupe Melon"),("Watermelon","Watermelon"),("Honeydew Melon","Honeydew Melon"),("Nectarine","Nectarine"),("Blood orange","Blood orange"),("Mandarine","Mandarine"),("Clementine Orange","Clementine Orange"),("Papaya","Papaya"),
    ("Passionfruit","Passionfruit"),("Peach","Peach"),("Pear","Pear"),("Persimmon","Persimmon"),("Plantain","Plantain"),("Prune","Prune"),("Pineapple","Pineapple"),("Plumcot","Plumcot"),("Pomegranate","Pomegranate"),("Pomelo","Pomelo"),("Raspberry","Raspberry"),("Redcurrant","Redcurrant"),("Strawberry","Strawberry"),("White currant","White currant")        
)

class Product(models.Model):
    product_name = models.CharField(max_length=200,choices=CHOICES,blank=False, default='artichoke')
    product_description = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1)],default=1)


    def __int__(self):
        #return "Farmer " + self.product_user.username + "\tProduct " + self.product_name
        return self.id
    

    
    def get_add_to_cart_url(self):
        print('1')
        return reverse("product_cart:add-to-cart", kwargs={
        "id": self.id
        })

    def get_remove_from_cart_url(self):
        print('1')
        return reverse("product_cart:remove-from-cart", kwargs={
        "id": self.id
        })

    product_picture = models.ImageField(blank=True, upload_to='images/')


class productReview(models.Model):
    review_title = models.CharField(max_length=30)
    review_message = models.CharField(max_length=200)
    review_product = models.IntegerField()

    def __str__(self):
        return "Product " + str(self.review_product) + "\ttitle " + self.review_title    