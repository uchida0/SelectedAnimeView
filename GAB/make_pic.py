from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import datetime
import tempfile
import shutil

def make_user_pic(cool, cool_view, num,anime_check_list):

    if "spring" in cool:
        color = (241,114,163)
    elif "summer" in cool:
        color = (247,234,65)
    elif "autumn" in cool:
        color = (246,102,0)
    elif "winter" in cool:
        color = (144,192,240)

    data_dir = "GAB/static/" + cool + "/"

    n = 6

    if num % n == 0:
        hn = num // n
    else:
        hn = (num // n) + 1
    
    im = Image.new("RGB", (160*n, 320*hn+160), color)
    draw = ImageDraw.Draw(im)
    ttfontname = "C:\\Windows\\Fonts\\meiryob.ttc"

    #cool_view
    cool_font = ImageFont.truetype(ttfontname, 100)
    draw.text((0,0), cool_view, font=cool_font, fill=(255,255,255))
    
    #作成日
    ts_font = ImageFont.truetype(ttfontname, 30)
    dt_now = datetime.datetime.now()
    ts = "作成日：" + dt_now.strftime("%Y/%m/%d")
    tsw, tsh = draw.textsize(ts, ts_font)
    draw.text((160*n-tsw, 160-tsh), ts, font=ts_font, fill=(255,255,255))

    #一時ファイルとして保存
    #tmpdir = tempfile.mkdtemp()
    tmpdir = "GAB/user"
    #tmpdir = "user"
    tmpdir = "GAB/static/user"
    im.save(tmpdir + "/" + cool + ".jpg")


    all_img = Image.open(tmpdir + "/" + cool +".jpg")
    back_im = all_img.copy()
    all_img.close()

    for i in range(1, num+1):
        #i_new = i+1
        img_dir = data_dir + str(i) + ".jpg"
        
        w_count = i % n - 1
        h_count = i // n
        if i % n == 0:
            w_count += n
            h_count -= 1
        
        #anime_check_listと照合して彩度を落とすかどうか
        anime_img = Image.open(img_dir)
        if str(i) not in anime_check_list:
            ns_anime = ImageEnhance.Brightness(anime_img)
            anime_img = ns_anime.enhance(0.3)

        back_im.paste(anime_img, (160*w_count, 320*h_count + 160))
    
    back_im.save(tmpdir+"/"+cool+".jpg")

    return tmpdir
