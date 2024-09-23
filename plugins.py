from requests import get,post
from os import name
from threading import Thread
from pytz import timezone
from datetime import date,datetime
import json 
from os import name
import os
from random import choice
from bs4 import BeautifulSoup
from re import findall
from PIL import Image, ImageDraw, ImageFont
from urllib.request import Request, urlopen
from urllib.parse import quote
from time import time
from rextester_Api import Rextester
import jdatetime
import pyPrivnote as pn

org = [":","0","1","2","3","4","5","6","7","8","9"]
fonts = [[":","𝟶","𝟷","𝟸","𝟹","𝟺","𝟻","𝟼","𝟽","𝟾","𝟿"],
[":","⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"],
[":","𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"],
[":","０","１","２","３","４","５","６","７","８","９"],
[":","₀","₁","₂","₃","₄","₅","₆","₇","₈","₉"],
[":","𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"]]
fonts2 = [[':','⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']]
org_eng = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
name_font = [["𝕬","𝕭","𝕮","𝕯","𝕰","𝕱","𝕲","𝕳","𝕴","𝕵","𝕶","𝕷","𝕸","𝕹","𝕺","𝕻","𝕼","𝕽","𝕾","𝕿","𝖀","𝖁","𝖂","𝖃","𝖄","𝖅"],
["𝓐","𝓑","𝓒","𝓓","𝓔","𝓕","𝓖","𝓗","𝓘","𝓙","𝓚","𝓛","𝓜","𝓝","𝓞","𝓟","𝓠","𝓡","𝓢","𝓣","𝓤","𝓥","𝓦","𝓧","𝓨","𝓩"],
["ꪖ","᥇","ᥴ","ᦔ","ꫀ","ᠻ","ᧁ","ꫝ","ⅈ","𝕛","𝕜","ꪶ","ꪑ","ꪀ","ꪮ","ρ","𝕢","𝕣","ડ","𝕥","ꪊ","ꪜ","᭙","᥊","ꪗ","𝕫"],
["𝔸","𝔹","ℂ","𝔻","𝔼","𝔽","𝔾","ℍ","𝕀","𝕁","𝕂","𝕃","𝕄","ℕ","𝕆","ℙ","ℚ","ℝ","𝕊","𝕋","𝕌","𝕍","𝕎","𝕏","𝕐","ℤ"],
["Ａ","Ｂ","Ｃ","Ｄ","Ｅ","Ｆ","Ｇ","Ｈ","Ｉ","Ｊ","Ｋ","Ｌ","Ｍ","Ｎ","Ｏ","Ｐ","Ｑ","Ｒ","Ｓ","Ｔ","Ｕ","Ｖ","Ｗ","Ｘ","Ｙ","Ｚ"],
["🄰","🄱","🄲","🄳","🄴","🄵","🄶","🄷","🄸","🄹","🄺","🄻","🄼","🄽","🄾","🄿","🅀","🅁","🅂","🅃","🅄","🅅","🅆","🅇","🅈","🅉"],
["Ⓐ","Ⓑ","Ⓒ","Ⓓ","Ⓔ","Ⓕ","Ⓖ","Ⓗ","Ⓘ","Ⓙ","Ⓚ","Ⓛ","Ⓜ","Ⓝ","Ⓞ","Ⓟ","Ⓠ","Ⓡ","Ⓢ","Ⓣ","Ⓤ","Ⓥ","Ⓦ","Ⓧ","Ⓨ","Ⓩ"],
["ᴬ","ᴮ","ᶜ","ᴰ","ᴱ","ᶠ","ᴳ","ᴴ","ᴵ","ᴶ","ᴷ","ᴸ","ᴹ","ᴺ","ᴼ","ᴾ","Q","ᴿ","ˢ","ᵀ","ᵁ","ⱽ","ᵂ","ˣ","ʸ","ᶻ"],
['ᴀ','ʙ','ᴄ','ᴅ','ᴇ','ꜰ','ɢ','ʜ','ɪ','ᴊ','ᴋ','ʟ','ᴍ','ɴ','ᴏ','ᴘ','Q','ʀ','ꜱ','ᴛ','ᴜ','ᴠ','ᴡ','x','ʏ','ᴢ'],
["ₐ","B","C","D","ₑ","F","G","ₕ","ᵢ","ⱼ","ₖ","ₗ","ₘ","ₙ","ₒ","ₚ","Q","ᵣ","ₛ","ₜ","ᵤ","ᵥ","W","ₓ","Y","Z"],
["𝐀","𝐁","𝐂","𝐃","𝐄","𝐅","𝐆","𝐇","𝐈","𝐉","𝐊","𝐋","𝐌","𝐍","𝐎","𝐏","𝐐","𝐑","𝐒","𝐓","𝐔","𝐕","𝐖","𝐗","𝐘","𝐙"],
["𝗔","𝗕","𝗖","𝗗","𝗘","𝗙","𝗚","𝗛","𝗜","𝗝","𝗞","𝗟","𝗠","𝗡","𝗢","𝗣","𝗤","𝗥","𝗦","𝗧","𝗨","𝗩","𝗪","𝗫","𝗬","𝗭"],
["卂","乃","匚","ᗪ","乇","千","Ꮆ","卄","丨","ﾌ","Ҝ","ㄥ","爪","几","ㄖ","卩","Ɋ","尺","丂","ㄒ","ㄩ","ᐯ","山","乂","ㄚ","乙"],
["A҉","B҉","C҉","D҉","E҉","F҉","G҉","H҉","I҉","J҉","K҉","L҉","M҉","N҉","O҉","P҉","Q҉","R҉","S҉","T҉","U҉","V҉","W҉","X҉","Y҉","Z҉"]]
Orgtarikh = ["/","0","1","2","3","4","5","6","7","8","9"]
ftarikh = [['/','⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.qqxnxx.com',
    'Origin': 'http://www.qqxnxx.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'
}
url = 'http://www.qqxnxx.com/download.php'

one = ["کیرم تو خارت", "بصیک بچه کونی", "بای بده ننه پولی", "کیرم تو ننت اوبی", "نگامت کص ننه ", "کص ننه پرده ارتجاعیت", "ننتو شبی چند میدی؟", "خارتو با روغن جامد گاییدم", "کص آبجیت ", "زنا زادع ", "ننه خیابونی", "گی ننه", "آبم لا کص ننت چجوری میشه", "بالا باش ننه کیر دزد", "ننت مجلسی میزنه؟کصصصص ننت جووووون", "ننه جریده", "گی پدر زنا زادع ", "ننتو کرایه میدی؟", "شل ننه بالا باش", "خارکصده به ننت بگو رو کیرم خوش میگذره؟", "ننه توله کص ننتو جر میدم", "بیا ننتو ببر زخمش کردم", "کص ننتو بزارم یکم بخندیم", "به ننت بگو بیاد واسم پر توف بزنه خرجتونو بدم یتیم", "فلج تیز باش ننتو بیار", "ننت پر توف میزنی بابات شم؟", "اوب کونی بزن به چاک تا ننتو جلوت حامله نکردمننه کون طلا بیا بالا", "یتیم بیا بغلم ", "ننت گنگ بنگ دوس داره؟", "بیا بگامت شاد شی خار کصده", "کیرم تو کص ننت بگو باشه", "داداش دوس داری یا آبجی ننه پولی", "۵۰ میدم ننتو بدهکیرم کص آبجی کص طلاااات", "ننه پولی چند سانت دوس داری؟", "دست و پا نزن ننه کص گشاد", "ننه ساکر هویت میخوای؟", "کیر سگا تو کص آبجیت ", "از ننت بپرس آب کیر پرتقالی دوس داره؟", "پستون ننت چنده", "تخخخخ بیا بالا ادبی", "مادرت دستو پا میزنه زیرم", "ننه سکسی بیا یه ساک بزن بخندیم", "خمینی اومد جاده دهاتتونو آسفالت کرد اومدید شهر و گرنه ننت کجا کص میداد؟", "گص کش", "کس ننه", "کص ننت", "کس خواهر", "کس خوار", "کس خارت", "کس ابجیت", "کص لیس", "ساک بزن", "ساک مجلسی", "ننه الکسیس", "نن الکسیس", "ناموستو گاییدم", "ننه زنا", "کس خل", "کس مخ", "کس مغز", "کس مغذ", "خوارکس", "خوار کس", "خواهرکس", "خواهر کس", "حروم زاده", "حرومزاده", "خار کس", "تخم سگ", "پدر سگ", "پدرسگ", "پدر صگ", "پدرصگ", "ننه سگ", "نن سگ", "نن صگ", "ننه صگ", "ننه خراب", "تخخخخخخخخخ", "نن خراب", "مادر سگ", "مادر خراب", "مادرتو گاییدم", "تخم جن", "تخم سگ", "مادرتو گاییدم", "ننه حمومی", "نن حمومی", "نن گشاد", "ننه گشاد", "نن خایه خور", "تخخخخخخخخخ", "نن ممه", "کس عمت", "کس کش", "کس بیبیت", "کص عمت", "کص خالت", "کس بابا", "کس خر", "کس کون", "کس مامیت", "کس مادرن", "مادر کسده", "خوار کسده", "تخخخخخخخخخ", "ننه کس", "بیناموس", "بی ناموس", "شل ناموس", "سگ ناموس", "ننه جندتو گاییدم باو ", "چچچچ نگاییدم سیک کن پلیز D:", "ننه حمومی", "چچچچچچچ", "لز ننع", "ننه الکسیس", "کص ننت", "بالا باش", "ننت رو میگام", "کیرم از پهنا تو کص ننت", "مادر کیر دزد", "ننع حرومی", "تونل تو کص ننت", "کیر تک تک بکس تلع گلد تو کص ننت", "کص خوار بدخواه", "خوار کصده", "ننع باطل", "حروم لقمع", "ننه سگ ناموس", "منو ننت شما همه چچچچ", "ننه کیر قاپ زن", "ننع اوبی", "ننه کیر دزد", "ننه کیونی", "ننه کصپاره", "زنا زادع", "کیر سگ تو کص نتت پخخخ", "ولد زنا", "ننه خیابونی", "هیس بع کس حساسیت دارم", "کص نگو ننه سگ که میکنمتتاااا", "کص نن جندت", "ننه سگ", "ننه کونی", "ننه زیرابی", "بکن ننتم", "ننع فاسد", "ننه ساکر", "کس ننع بدخواه", "نگاییدم", "مادر سگ", "ننع شرطی", "گی ننع", "بابات شاشیدتت چچچچچچ", "ننه ماهر", "حرومزاده", "ننه کص", "کص ننت باو", "پدر سگ", "سیک کن کص ننت نبینمت", "کونده", "ننه ولو", "ننه سگ", "مادر جنده", "کص کپک زدع", "ننع لنگی", "ننه خیراتی", "سجده کن سگ ننع", "ننه خیابونی", "ننه کارتونی", "تکرار میکنم کص ننت", "تلگرام تو کس ننت", "کص خوارت", "خوار کیونی", "پا بزن چچچچچ", "مادرتو گاییدم", "گوز ننع", "کیرم تو دهن ننت", "ننع همگانی", "کیرم تو کص زیدت", "کیر تو ممهای ابجیت", "ابجی سگ", "کس دست ریدی با تایپ کردنت چچچ", "ابجی جنده", "ننع سگ سیبیل", "بده بکنیم چچچچ", "کص ناموس", "شل ناموس", "ریدم پس کلت چچچچچ", "ننه شل", "ننع قسطی", "ننه ول", "دست و پا نزن کس ننع", "ننه ولو", "خوارتو گاییدم", "محوی!؟", "ننت خوبع!؟", "کس زنت", "شاش ننع", "ننه حیاطی \\\\\/:", "نن غسلی", "کیرم تو کس ننت بگو مرسی چچچچ", "ابم تو کص ننت :\\\\\/", "فاک یور مادر خوار سگ پخخخ", "کیر سگ تو کص ننت", "کص زن", "ننه فراری", "بکن ننتم من باو جمع کن ننه جنده \\\\\/:::", "ننه جنده بیا واسم ساک بزن", "حرف نزن که نکنمت هااا :|", "کیر تو کص ننت😐", "کص کص کص ننت", "کصصصص ننت جووون", "سگ ننع", "کص خوارت", "کیری فیس", "کلع کیری", "تیز باش سیک کن نبینمت", "فلج تیز باش چچچ", "بیا ننتو ببر", "بکن ننتم باو ", "کیرم تو بدخواه", "چچچچچچچ", "ننه جنده", "ننه کص طلا", "ننه کون طلا", "کس ننت بزارم بخندیم!؟", "کیرم دهنت", "مادر خراب", "ننه کونی", "هر چی گفتی تو کص ننت خخخخخخخ", "کص ناموست بای", "کص ننت بای :\\\\\/\\\\\/", "کص ناموست باعی تخخخخخ", "کون گلابی!", "ریدی آب قطع", "کص کن ننتم کع", "نن کونی", "نن خوشمزه", "ننه لوس", " نن یه چشم ", "ننه چاقال", "ننه جینده", "ننه حرصی ", "نن لشی", "ننه ساکر", "نن تخمی", "ننه بی هویت", "نن کس", "نن سکسی", "نن فراری", "لش ننه", "سگ ننه", "شل ننه", "ننه تخمی", "ننه تونلی", "ننه کوون", "نن خشگل", "نن جنده", "نن ول ", "نن سکسی", "نن لش", "کس نن ", "نن کون", "نن رایگان", "نن خاردار", "ننه کیر سوار", "نن پفیوز", "نن محوی", "ننه بگایی", "ننه بمبی", "ننه الکسیس", "نن خیابونی", "نن عنی", "نن ساپورتی", "نن لاشخور", "ننه طلا", "ننه عمومی", "ننه هر جایی", "نن دیوث", "تخخخخخخخخخ", "نن ریدنی", "نن بی وجود", "ننه سیکی", "ننه کییر", "نن گشاد", "نن پولی", "نن ول", "نن هرزه", "ننه لاشی کیری", "ننه ویندوزی", "نن تایپی", "نن برقی", "نن شاشی", "ننه درازی", "شل ننع", "یکن ننتم که", "کس خوار بدخواه", "آب چاقال", "ننه جریده", "ننه سگ سفید", "آب کون", "ننه 85", "ننه سوپری", "بخورش", "کس ن", "خوارتو گاییدم", "خارکسده", "گی پدر", "آب چاقال", "زنا زاده", "زن جنده", "سگ پدر", "مادر جنده", "ننع کیر خور", "چچچچچ", "تیز بالا", "ننه سگو با کسشر در میره", "کیر سگ تو کص ننت", "kos kesh", "kir", "kiri", "nane lashi", "kos", "kharet", "blis kirmo", "اوبی کونی هرزه", "کیرم لا کص خارت", "کیری", "ننه لاشی", "ممه", "کص", "کیر", "بی خایه", "ننه لش", "بی پدرمادر", "خارکصده", "مادر جنده", "کصکش", "کیرم کون مادرت", "بالا باش کیرم کص مادرت", "مادرتو میگام نوچه جون بالا??", "اب خارکصته تند تند تایپ کن ببینم", "مادرتو میگام بخای فرار کنی", "لال شو", "کیرم تو خارت", "بصیک بچه کونی", "بای بده ننه پولی", "کیرم تو ننت اوبی", "نگامت کص ننه ", "کص ننه پرده ارتجاعیت", "ننتو شبی چند میدی؟", "خارتو با روغن جامد گاییدم", "کص آبجیت ", "زنا زادع ", "ننه خیابونی", "گی ننه", "آبم لا کص ننت چجوری میشه", "بالا باش ننه کیر دزد", "ننت مجلسی میزنه؟", "کصصصص ننت جووووون", "ننه جریده", "گی پدر زنا زادع ", "ننتو کرایه میدی؟", "شل ننه بالا باش", "خارکصده به ننت بگو رو کیرم خوش میگذره؟", "ننه توله کص ننتو جر میدم", "بیا ننتو ببر زخمش کردم", "کص ننتو بزارم یکم بخندیم", "به ننت بگو بیاد واسم پر توف بزنه خرجتونو بدم یتیم", "ننه کون طلا بیا بالا", "یتیم بیا بغلم ", "ننت گنگ بنگ دوس داره؟", "بیا بگامت شاد شی خار کصده", "کیرم تو کص ننت بگو باشه", "داداش دوس داری یا آبجی ننه پولی", "۵۰ میدم ننتو بده", "فلج تیز باش ننتو بیار", "کیرم کص آبجی کص طلاااات", "ننه پولی چند سانت دوس داری؟", "دست و پا نزن ننه کص گشاد", "ننه ساکر هویت میخوای؟", "کیر سگا تو کص آبجیت ", "از ننت بپرس آب کیر پرتقالی دوس داره؟", "پستون ننت چنده", "تخخخخ بیا بالا ادبی", "مادرت دستو پا میزنه زیرم", "ننه سکسی بیا یه ساک بزن بخندیم", "خمینی اومد جاده دهاتتونو آسفالت کرد اومدید شهر و گرنه ننت کجا کص میداد؟", "کیرم تا ته و از پهنا تو کص مادرت", "کص ناموس مادرت", "مادر کص پاپیونی ", "مادر جنده حروم تخمی", "اوبی زاده حقیر", "بابات زیر کیرم بزرگ شد", "اسمم رو کون مادرت تتو شده", "خیخیخیخیخی", "چچچچچچچچ", "زجه بزن ناموس گلابی", "مادرت کیرمه ", "بابات منم ", "تخم سگ حروم زاده ", "کص ناموست ", "خواهرتو گاییدم", "ریدم بهت بیشعور", " بی شرف", " ریدم تو مغزت", " بی ارزش", " کصکش", " ریدم توی ناموست", " بی ناموس", " مادرجنده", " خواهر کصکش", " ریدم توی کل طایفت", " بی ناموس برو", " خوشم ازت نمیاد کصکش", " تو کصکشی", " برو خواهر جنده", "برو مادرجنده", " برو برادر کونی", " کونکش", "عوض بی ناموس", "ریدم تو قبر مادرت", "ریدم تو قبر پدرت", " ریدم تو قبرت", " ریدم تو زاتت", " ریدم تو خواهر جنده", " خواهر جندت خوبه", " مادر جندت خوبه", " پدر کونکشت خوبه", "برادر کونیت خوب", " پدرسگ", " مادر سگ", " برادر سگ", " خواهر سگ", " خواهر جندت چی", " مادر جندت چی", " پدر کونیت چی", " برادر کونیت چی", " اره جنده ها", " تو جنده ای", " تو کونی ای", " توی کصکشی", " خوشم از جنده ها نمیاد", " خواهرت جنده شده", " مادرت جنده شده", " جنده برو خودت رو جمع کن", " مامانت امشب روی کی هستش", " خواهرت پیش کیه", " برادرت داره کجا کون میده", " بابای قرمساقت کو", " خواهرت امشب روی کی هستش", " مادرت امشب روی کی خوابیده", "ننت پر توف میزنی بابات شم؟", "اوب کونی بزن به چاک تا ننتو جلوت حامله نکردم", " ریدم بهت", " بیشعور", " بی شرف", " ریدم تو مغزت", " بی ارزش", " کصکش", " ریدم توی ناموست", " بی ناموس", " مادرجنده", " خواهر کصکش", " ریدم توی کل طایفت", " بی ناموس برو", " خوشم ازت نمیاد کصکش", " تو کصکشی", " برو خواهر جنده", " برو مادرجنده", " برو برادر کونی", " کونکش", " عوض بی ناموس", " ریدم تو قبر مادرت", " ریدم تو قبر پدرت", " ریدم تو قبرت", " ریدم تو زاتت", " ریدم تو خواهر جنده", " خواهر جندت خوبه", " مادر جندت خوبه", " پدر کونکشت خوبه", " برادر کونیت خوب", " پدرسگ", " مادر سگ", " برادر سگ", " خواهر سگ", " خواهر جندت چی", " مادر جندت چی", " پدر کونیت چی", " برادر کونیت چی", " اره جنده ها", " تو جنده ای", " تو کونی ای", " توی کصکشی", " خوشم از جنده ها نمیاد", " خواهرت جنده شده", " مادرت جنده شده", " جنده برو خودت رو جمع کن", " مامانت امشب روی کی هستش", " خواهرت پیش کیه", " برادرت داره کجا کون میده", " بابای قرمساقت کو", " خواهرت امشب روی کی هستش", " مادرت امشب روی کی خوابیده", "کیرم کون مادرت", "بالا باش کیرم کص مادرت", "مادرتو میگام نوچه جون بالا", "اب خارکصته تند تند تایپ کن ببینم", "مادرتو میگام بخای فرار کنی", "لال شو دیگه نوچه", "مادرتو میگام اف بشی", "کیرم کون مادرت", "کیرم کص مص مادرت بالا", "کیرم تو چشو چال مادرت", "کون مادرتو میگام بالا", "بیناموس  خسته شدی؟", "نبینم خسته بشی بیناموس", "ننتو میکنم", "کیرم کون مادرت ", "صلف تو کصننت بالا", "بیناموس بالا باش بهت میگم", "کیر تو مادرت", "کص مص مادرتو بلیسم؟", "کص مادرتو چنگ بزنم؟", "به خدا کصننت بالا ", "مادرتو میگام ", "کیرم کون مادرت بیناموس", "مادرجنده بالا باش", "بیناموس تا کی میخای سطحت گح باشه", "اپدیت شو بیناموس خز بود", "کیرم از پهنا تو ننت", "و اما تو بیناموس چموش", "تو یکیو مادرتو میکنم", "کیرم تو ناموصت ", "کیر تو ننت", "ریش روحانی تو ننت", "کیر تو مادرت", "کص مادرتو مجر بدم", "صلف تو ننت", "بات تو ننت ", "مامانتو میکنم بالا", "کیر ترکا به ناموست", "سطحشو نگا", "تایپ کن بیناموس", "خشاب؟", "کیرم کون مادرت بالا", "بیناموس نبینم خسته بشی", "مادرتو بگام؟", "گح تو سطحت شرفت رف", "بیناموس شرفتو نابود کردم یه کاری کن", "وای کیرم تو سطحت", "بیناموس روانی شدی", "روانیت کردما", "مادرتو کردم کاری کن", "تایپ تو ننت", "بیپدر بالا باش", "و اما تو لر خر", "ننتو میکنم بالا باش", "کیرم لب مادرت بالا", "چطوره بزنم نصلتو گح کنم", "داری تظاهر میکنی ارومی ولی مادرتو کوص کردم", "مادرتو کردم بیغیرت", "هرزه", "وای خدای من اینو نگا", "کیر تو کصننت", "ننتو بلیسم", "منو نگا بیناموس", "کیر تو ننت بسه دیگه", "خسته شدی؟", "ننتو میکنم خسته بشی", "وای دلم کون مادرت بگام", "اف شو احمق", "بیشرف اف شو بهت میگم", "مامان جنده اف شو", "کص مامانت اف شو", "کص لش وا ول کن اینجوری بگو؟", "ای بیناموس چموش", "خارکوصته ای ها", "مامانتو میکنم اف نشی", "گح تو ننت", "سطح یه گح صفتو", "گح کردم تو نصلتا", "چه رویی داری بیناموس", "ناموستو کردم", "رو کص مادرت کیر کنم؟", "نوچه بالا", "کیرم تو ناموصتاا", "یا مادرتو میگام یا اف میشی", "لالشو دیگه", "بیناموس", "مادرکصته", "ناموص کصده", "وای بدو ببینم میرسی", "کیرم کون مادرت چیکار میکنی اخه", "خارکصته بالا دیگه عه", "کیرم کصمادرت", "کیرم کون ناموصد", "بیناموس من خودم خسته شدم توچی؟", "ای شرف ندار", "مامانتو کردم بیغیرت", "و اما مادر جندت", "تو یکی زیر باش", "اف شو", "خارتو کوص میکنم", "کوصناموصد", "ناموص کونی", "خارکصته ی بۍ غیرت", "شرم کن بیناموس", "مامانتو کرد ", "ای مادرجنده", "بیغیرت", "کیرتو ناموصت", "بیناموس نمیخای اف بشی؟", "ای خارکوصته", "لالشو دیگه", "همه کس کونی", "حرامزاده", "مادرتو میکنم", "بیناموس", "کصشر", "اف شو مادرکوصته", "خارکصته کجایی", "ننتو کردم کاری نمیکنی؟", "کیرتو مادرت لال", "کیرتو ننت بسه", "کیرتو شرفت", "مادرتو میگام بالا", "کیر تو مادرت", "کونی ننه ی حقیر زاده", "وقتی تو کص ننت تلمبه های سرعتی میزدم تو کمرم بودی بعد الان برا بکنه ننت شاخ میشی هعی   ", "تو یه کص ننه ای ک ننتو به من هدیه کردی تا خایه مالیمو کنی مگ نه خخخخ", "انگشت فاکم تو کونه ناموست", "تخته سیاهه مدرسه با معادلات ریاضیه روش تو کص ننت اصلا خخخخخخخ ", "کیرم تا ته خشک خشک با کمی فلفل روش تو کص خارت ", "کص ننت به صورت ضربدری ", "کص خارت به صورت مستطیلی", "رشته کوه آلپ به صورت زنجیره ای تو کص نسلت خخخخ ", "10 دقیقه بیشتر ابم میریخت تو کس ننت این نمیشدی", "فکر کردی ننت یه بار بهمـ داده دیگه شاخی", "اگر ننتو خوب کرده بودم حالا تو اینجوری نمیشدی"]
onee = ["❤️", "🧡", "💛", "💚", "🩵", "💜", "🩶", "🤍"]

def fosh_saz(text):
 return f"{choice(one)}{text}"
 
def ghalb_saz(text):
 return f"{choice(onee)}{text}"

def font(text, lang):
 request = get('https://api.codebazan.ir/font/?type={}&text={}'.format(lang, text))
 if request.json()['Ok' if lang else 'ok'] == True:
  results = "🌜 ᴛʜᴇʀᴇ's ʏᴏᴜʀ ʀᴇsᴜʟᴛ 🌛 \n\n"
  for key, value in request.json()['Result' if lang else 'result'].items():
   results += f"├ • {key} | `{value}`\n"
 return results

def create_time():
 a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
 ran = choice(fonts)
 for char in a :
  a = a.replace(char , ran[int(org.index(str(char)))])
 return a

def create_time2():
 a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")
 ran = choice(fonts2)
 for char in a :
  a = a.replace(char , ran[int(org.index(str(char)))])
 return a

def create_tarikh():
 a = jdatetime.date.today().strftime("%Y/%m/%d")
 ran = choice(ftarikh)
 for char in a :
  a = a.replace(char , ran[int(Orgtarikh.index(str(char)))])
 return a

def fontinname(name):
 name = name.upper()
 rnd = choice(name_font)
 for char in name:
  try:
   name = name.replace(char , rnd[org_eng.index(char)])
  except:
   pass
 return name

def DLX(Url):
    data = {'videoid': Url}
    soup = BeautifulSoup(post(url=url, headers=headers, data=data).text, 'html.parser')
    link = findall(r'"(https://video-hw.xnxx-cdn.com/videos/flv/.*)"', str(soup.find('script', {'type': 'application/ld+json'})))[0].split('"')[0]
    FileName = link.split('/')[-1]
    FileName = FileName[:FileName.find('?')]
    return link

def snippet(params):
    url = 'https://api.crabon.io/v1/snippet'
    path = 'i.png'
    response = post('https://carbonara-42.herokuapp.com/api/cook', json=params)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
    print(response.status_code)
    
def generateimage(text):
    rand_img = ["image1.jpg","image2.jpg","image3.jpg","image4.jpg","image5.jpg","image6.jpg"]
    image = Image.open(choice(rand_img))
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='font.ttf', size=190)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill=choice(["#00c7a4","#0071c7","#c7a200","#728593","#943633","#6495ed","#43f70a","#e1b2ae","#527130","#629f5d","#3d4e90","#9a9ec4",]))
    image.save('time_image.jpg')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def if_not_exist_creat(filename):
 if not os.path.isfile(filename):
  with open(filename , "w") as f:
   f.write("")
   f.close() 
def write(filename , text):
 with open(filename , "w", encoding="utf-8") as f:
   f.write(text)
   f.close() 
def write_a(filename , text):
 with open(filename , "a", encoding="utf-8") as f:
   f.write(text)
   f.close() 
def read(filename):
 with open(filename , "r", encoding="utf-8") as f:
   return f.read()
def json_read(filename):
 with open(filename , "r", encoding="utf-8") as f:
   return json.load(f)
   
def run_codi(lang , code):
    a = Rextester(lang , code)
    k = a.stats;k = k.replace(",","")
    run_time = k.index("running time:")
    cpu_time = k.index("cpu time:")
    used_memory = k.index("memory peak:")
    kossher = k.index("absolute service time")
    mamad = f"**Result**: \n`{a.result if a.result else '--'}`{f'**ERROR**: `{a.errors}`' if a.errors else ''}\n**State**:\n__{k[run_time:cpu_time]}\n{k[cpu_time:used_memory]}\n{k[used_memory:kossher]}__"
    return mamad

def moon_or_sun():
  a = datetime.now(timezone("Asia/Tehran")).strftime("%H");a = int(a)
  if a in[20,21,22,23,00,1,2,3,4,5]:
    b = "🌑"
  elif a in[6,7]:
    b = "🌒"
  elif a in[8,9,10,11]:
    b = "🌔"
  elif a in[12,13,14,15,16,17]:
    b = "🌕"
  elif a in[18,19]:
    b = "🌒"
  return b

def dast_del(text):
  if text.privileges:
     if text.privileges.can_delete_messages == True:
        return True

def have_sec(t):
  if len(t.split(":")) == 3:
    return str(t)
  else:
    return str(t) +":00"
    
def read_note(url):
  b = str()   
  for j in url.split("\n"):
    try: 
      n = pn.read_note(j) 
      b += f"\n({j}) --> ({n})"
    except Exception as er:
      b += f"\n({j}) --> ({er})"
  return b


