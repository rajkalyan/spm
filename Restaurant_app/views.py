from django.db.models.fields import DecimalField
from Restaurant_app.models import  Breads, Manageorders, Order, Orderhistory, Rice, Rolereq, Starters, User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Restaurant_app.forms import Breadsform, Pfupd, Riceform, Rlupd, Startersform, usgform, Rltype,Chgepwd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Restaurant import settings
from decimal import Decimal
# Create your views here.
def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')

def login(request):
    return render(request,'app/login.html')

def usrreg(request):
    if request.method == "POST":
        d = usgform(request.POST)
        if d.is_valid():
            d.save()
            return redirect('/login')
    d=usgform()
    return render(request,'app/userregister.html',{'t':d})


@login_required
def additems(request):      
    return render(request,'app/additems.html')

@login_required
def addstarter(request):
    if request.method == "POST":
        k = Startersform(request.POST,request.FILES)
        if k.is_valid():
            k.save()
            messages.success(request,"Item added Successfully")
            return redirect('/additems')
    k=Startersform(request.FILES) 
    return render(request,'app/addstarter.html',{'r':k})

@login_required
def addbreads(request):
    if request.method == "POST":
        k = Breadsform(request.POST,request.FILES)
        if k.is_valid():
            k.save()
            messages.success(request,"Item added Successfully")
            return redirect('/additems')
    k=Breadsform(request.FILES)
    return render(request,'app/addbreads.html',{'r':k})

@login_required
def addrab(request):
    if request.method == "POST":
        k = Riceform(request.POST,request.FILES)
        if k.is_valid():
            k.save()
            messages.success(request,"Item added Successfully")
            return redirect('/additems')
    k=Riceform(request.FILES)
    return render(request,'app/addrab.html',{'r':k})
@login_required
def orders(request):
    a = Starters.objects.all()
    b = Breads.objects.all()
    d = Rice.objects.all()
    if request.method == "POST":
        iname = request.POST['itemname']
        iprice = request.POST['itemprice']
        iquant = request.POST['qt']
        q = Order(name = iname, price =iprice, quantity =iquant,uid_id=request.user.id)
        q.save()
        return redirect('/orders')
    return render(request,'app/orders.html',{'starters':a,'breads':b,'rice':d})

@login_required
def accept(request):
    a = Order.objects.filter(uid_id=request.user.id)
    strn=""
    tp=0
    tax=float(0.18)
    for j in a:
        tp = tp + (j.price*j.quantity)
    gt = float(tp)+(float(tp)*tax)
    for i in a:
        strn = strn + i.name + "(" +str(i.quantity) + ")" + ","
    return render(request,'app/orderaccept.html',{'orders':a})

@login_required
def bill(request):
    a = Order.objects.filter(uid_id=request.user.id)
    tp=0
    tot=0
    tax=float(0.18)
    taxes = 0
    for i in a:
        tp = tp + (i.price*i.quantity)
    gt = float(tp)+(float(tp)*tax)
    taxes = gt-float(tp)
    tot = gt-taxes
    strn = ""
    for i in a:
        strn = strn + i.name + "(" +str(i.quantity) + ")" + ","
    if request.method == "POST":   
        w = Orderhistory(items=strn,billamoubt=gt, cid_id=request.user.id)
        w.save()
        name=request.POST['Cname']
        tablenum = request.POST['tn']
        s = Manageorders(uname=name,tname=tablenum,items=strn)
        s.save()
        a.delete()
        return redirect('/orders')
    return render(request,'app/bill.html',{'orders':a,'gt':gt,'taxes':taxes,'tot':tot})

@login_required
def od(request,n):
    r=Manageorders.objects.get(id=n)
    if request.method=="POST":
        r.delete()
        return redirect('/po')
    return render(request,'app/od.html')

@login_required
def oh(request):
    a = Orderhistory.objects.filter(cid_id=request.user.id)
    return render(request,'app/oh.html',{'oh':a})

@login_required
def id(request,n):
    r=Order.objects.get(id=n)
    if request.method=="POST":
        r.delete()
        return redirect('/accept')
    return render(request,'app/id.html')

@login_required
def iup(request,n):
    t = Order.objects.get(id=n)
    ct = 0
    ct = (t.price*t.quantity)
    print(ct)
    if request.method == "POST":
        newquantity = request.POST['n']
        t.quantity = newquantity
        t.save()
        return redirect('/accept')
    return render(request,'app/iup.html',{'p':t,'ct':ct})

@login_required
def po(request):
    a = Manageorders.objects.all()
    return render(request,'app/po.html',{'orders':a})

@login_required
def rolereq(request):
    p = Rolereq.objects.filter(ud_id=request.user.id).count()
    if request.method == "POST":
        k = Rltype(request.POST,request.FILES)
        if k.is_valid():
            y = k.save(commit=False)
            y.ud_id = request.user.id
            y.uname = request.user.username
            y.is_checked = 0
            print(y)
            y.save()
            # return redirect('/')
    k = Rltype()
    return render(request,'app/rolereq.html',{'d':k, 'c':p})

@login_required
def gveperm(request):
    u = User.objects.all()
    r = Rolereq.objects.all()
    d={}
    for n in u:
        for m in r:
            if n.is_superuser == 1 or n.id != m.ud_id :
                continue
            else:
                d[m.id] = m.Uname, m.rltype, n.role,n.id,m.id
    return render(request,'app/gvpl.html',{'h':d.values()})

@login_required
def gvupd(request,t):
    y = Rolereq.objects.get(ud_id=t)
    d = User.objects.get(id=t)
    if request.method == "POST":
        n = Rlupd(request.POST,instance=d)
        if n.is_valid():
            n.save()
            y.is_checked = 1
            y.save()
            return redirect('/gvper')
    n = Rlupd(instance=d)
    return render(request,'app/gvepermission.html',{'c':n})

@login_required
def gvdel(request,m):
    r = Rolereq.objects.get(id=m)
    a = User.objects.get(id = r.ud_id)
    if request.method == "POST":
        a.role=1
        r.delete()
        a.save()
        messages.success(request,"{} Request Deleted Successfully".format(a.username))
        return redirect('/gvper')
    n = Rlupd(instance=r)
    return render(request,'app/gvdel.html',{'a':n})

@login_required
def pfle(request):
    y = User.objects.get(id=request.user.id)
    return render(request,'app/profile.html',{'q':y})

@login_required
def pfupd(request):
	t = User.objects.get(id=request.user.id)
	if request.method == "POST":
		pfl = Pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')
	pfl = Pfupd(instance=t)
	return render(request,'app/profileupdate.html',{'u':pfl})


@login_required
def feedback(request):
    if request.method == "POST":
        sd = request.POST['snmail'].split(',')
        sm = request.POST['sub']
        mg = request.POST['msg']
        rt = settings.EMAIL_HOST_USER
        dt = send_mail(sm,mg,rt,sd)
        if dt == 1:
            return redirect('/')
    return render(request,'app/feedback.html')

@login_required
def changepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})

