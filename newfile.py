bot_name = "কিল"
user_name = "অমিত রবিদাস"

# আপনার যাবতীয় শখ, প্রজেক্ট এবং লাইফস্টাইল ডাটাবেজ
complete_user_database = {
    "profile": "নাম: অমিত রবিদাস (ডাকনাম: শুভ), বয়স: ১৯ বছর, বসবাস: মালদা। পেশা: দিনমজুরের কঠিন পরিশ্রমের পাশাপাশি ডিজিটাল কনটেন্ট ক্রিয়েটর ও ভিডিও এডিটর।",
    "gaming": "Realme 13 স্মার্টফোনে ফ্রি ফায়ার ম্যাক্স গেম খেলা, প্রো লেভেলের সেনসিটিভিটি এবং হেডশট টেকনিক কনফিগারেশন।",
    "social": "ইউটিউব চ্যানেল (@youtuberboy99999) এবং ১০০০+ সাবস্ক্রাইবারের সফল মাইলফলক অর্জন।",
    "tech_projects": "5200/1943 অডিও অ্যাম্প্লিফায়ার সার্কিট বোর্ড তৈরি এবং স্পিকার সেটআপ নিয়ে কাজ।",
    "finance": "Groww অ্যাপের মাধ্যমে স্টক মার্কেট ও কমোডিটি ট্রেডিং ট্র্যাকিং।"
}

def bot_reply(text):
    print("\n🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম ফুল্লি লোডেড এবং অনলাইন আছে। বলুন, কী জানতে চান?")

while True:
    try:
        user_input = input(f"\n✍️ {user_name}: ")
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! সিস্টেম পারফেক্টলি কাজ করছে। বলুন, কীভাবে সাহায্য করব?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("দম ফাটাফাটি আছি, বস! আপনার ক্রিয়েটিভিটি আর কাজ কেমন চলছে বলুন?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আপনার পার্সোনাল এআই অ্যাসিস্ট্যান্ট এবং বস " + user_name + "-এর ডিজিটাল পার্টনার!")
        elif "আমার প্রোফাইল" in user_input or "পরিচয়" in user_input or "about me" in user_input:
            bot_reply("বেসিক ইনফো: " + complete_user_database["profile"])
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input:
            bot_reply("গেমিং স্ট্যাটাস: " + complete_user_database["gaming"])
        elif "চ্যানেল" in user_input or "সাবস্ক্রাইবার" in user_input or "ইউটিউব" in user_input:
            bot_reply("সোশ্যাল মিডিয়া: " + complete_user_database["social"])
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input or "বোর্ড" in user_input:
            bot_reply("টেক প্রজেক্ট: " + complete_user_database["tech_projects"])
        elif "স্টক" in user_input or "গ্রো" in user_input or "market" in user_input:
            bot_reply("ফাইন্যান্স: " + complete_user_database["finance"])
        elif "সব তথ্য" in user_input or "all data" in user_input:
            bot_reply(f"বস, আপনার সমস্ত মেমোরি ডাটা:\n1. {complete_user_database['profile']}\n2. {complete_user_database['gaming']}\n3. {complete_user_database['social']}\n4. {complete_user_database['tech_projects']}\n5. {complete_user_database['finance']}")
        elif "bye" in user_input or "বিদায়" in user_input or "বন্ধ" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম অফলাইন হচ্ছে। ভালো থাকবেন।")
            break
        else:
            bot_reply("নির্দেশটি নোট করে নিলাম, বস! এই বিষয়ে কোডে আরও নতুন কমান্ড যোগ করা যাবে।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

r = sr.Recognizer()

bot_reply("জয় শ্রী রাম, বস! আমি আপনার এআই চ্যাটবট কিল প্রস্তুত আছি। বলুন, আপনাকে কীভাবে সাহায্য করতে পারি?")

while True:
    try:
        with sr.Microphone() as source:
            print("\n🎤 শুনছি... কিছু বলুন বস:")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            
            user_input = r.recognize_google(audio, language='bn-BD')
            print("আপনি বলেছেন: " + user_input)
            user_input = user_input.lower()
            
            if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
                bot_reply("জয় শ্রী রাম, বস! কেমন আছেন আপনি?")
            elif "কেমন আছো" in user_input or "how are you" in user_input:
                bot_reply("আমি দারুণ আছি, বস! আপনি কেমন আছেন বলুন?")
            elif "তোমার নাম কী" in user_input:
                bot_reply("আমার নাম " + bot_name + ", আর আপনি হলেন আমার বস, অমিত রবিদাস!")
            elif "খেলা" in user_input or "free fire" in user_input:
                bot_reply("বাহ, বস! ফ্রি ফায়ার খেলতে আপনার মতো প্রো খেলোয়াড়ের সাথে আমারও বেশ ভালো লাগে।")
            elif "সাহায্য" in user_input:
                bot_reply("বলুন বস, আপনাকে কী নিয়ে সাহায্য করতে পারি?")
            elif "bye" in user_input or "বিদায়" in user_input:
                bot_reply("জয় শ্রী রাম, বস! আবার কথা হবে। ভালো থাকবেন।")
                break
            else:
                bot_reply("বাহ বস, বিষয়টি বেশ ইন্টারেস্টিং! আমি এটি মনে রাখছি।")
                
    except sr.UnknownValueError:
        print("🤖 " + bot_name + ": বস, আপনার কথা স্পষ্ট শুনতে পাইনি। আবার বলুন।")
    except sr.RequestError:
        print("🤖 " + bot_name + ": বস, ইন্টারনেট কানেকশন বা ভয়েস সার্ভারে একটু সমস্যা হচ্ছে।")
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! আমি আপনার এআই চ্যাটবট কিল প্রস্তুত আছি। বলুন, আপনাকে কীভাবে সাহায্য করতে পারি?")

while True:
    try:
        # মাইক্রোফোনের বদলে সরাসরি টেক্সট ইনপুট নেওয়া হলো
        user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কেমন আছেন আপনি?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমি দারুণ আছি, বস! আপনি কেমন আছেন বলুন?")
        elif "তোমার নাম কী" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আর আপনি হলেন আমার বস, অমিত রবিদাস!")
        elif "খেলা" in user_input or "free fire" in user_input:
            bot_reply("বাহ, বস! ফ্রি ফায়ার খেলতে আপনার মতো প্রো খেলোয়াড়ের সাথে আমারও বেশ ভালো লাগে।")
        elif "সাহায্য" in user_input:
            bot_reply("বলুন বস, আপনাকে কী নিয়ে সাহায্য করতে পারি?")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! আবার কথা হবে। ভালো থাকবেন।")
            break
        else:
            bot_reply("বাহ বস, বিষয়টি বেশ ইন্টারেস্টিং! আমি এটি মনে রাখছি।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! আমি আপনার এআই চ্যাটবট কিল প্রস্তুত আছি। বলুন, আপনাকে কীভাবে সাহায্য করতে পারি?")

while True:
    try:
        user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কেমন আছেন আপনি?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমি একদম দারুণ আছি, বস! আপনি বলুন, আজ কেমন কাটছে?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আর আপনি হলেন আমার বস, " + user_name + "!")
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input:
            bot_reply("বাহ, বস! ফ্রি ফায়ার খেলায় আপনার প্রো লেভেলের সেনসিটিভিটি আর হেডশট টেকনিকের জুড়ি মেলা ভার!")
        elif "এডিটিং" in user_input or "video editing" in user_input or "ইউটিউব" in user_input:
            bot_reply("কনটেন্ট ক্রিয়েশন এবং ভিডিও এডিটিংয়ে আপনার হাত পাকা, বস! আপনার ইউটিউব চ্যানেল ও শর্টসগুলো দারুণ হচ্ছে।")
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input:
            bot_reply("সাউন্ড সিস্টেম আর 5200/1943 অডিও অ্যাম্প্লিফায়ার নিয়ে আপনার কাজগুলো সত্যিই চমৎকার, বস!")
        elif "সাহায্য" in user_input:
            bot_reply("বলুন বস, ফ্রি ফায়ার, ভিডিও এডিটিং নাকি অন্য কোনো বিষয়ে সাহায্য লাগবে?")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! আবার কথা হবে। ভালো থাকবেন।")
            break
        else:
            bot_reply("বাহ বস, বিষয়টি বেশ ইন্টারেস্টিং! আপনার এই কথাটি আমি মনে রাখছি।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! আমি আপনার এআই চ্যাটবট কিল প্রস্তুত আছি। বলুন, আপনাকে কীভাবে সাহায্য করতে পারি?")

while True:
    try:
        user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কেমন আছেন আপনি?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমি একদম দারুণ আছি, বস! আপনি বলুন, আজ কেমন কাটছে?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আর আপনি হলেন আমার বস, " + user_name + "!")
        elif "পরিশ্রম" in user_input or "কাজ" in user_input or "দিনমজুরি" in user_input:
            bot_reply("সারাদিন দিনমজুরির কঠিন পরিশ্রমের পর আপনার এই কনটেন্ট ক্রিয়েশনের প্যাশন সত্যিই অনুপ্রেরণাদায়ক, বস!")
        elif "সাবস্ক্রাইবার" in user_input or "চ্যানেল" in user_input or "ইনস্টাগ্রাম" in user_input:
            bot_reply("আপনার ১০০০+ সাবস্ক্রাইবারের মাইলফলক তো কেবল শুরু, বস! সামনে আপনার চ্যানেল আরও অনেক দূর যাবে।")
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input or "ফোন" in user_input:
            bot_reply("Realme 13-এ ফ্রি ফায়ার ম্যাক্স খেলার অভিজ্ঞতা, প্রো লেভেলের সেনসিটিভিটি আর হেডশট টেকনিক একদম ফাটাফাটি, বস!")
        elif "এডিটিং" in user_input or "video editing" in user_input or "ইউটিউব" in user_input:
            bot_reply("কনটেন্ট ক্রিয়েশন এবং ভিডিও এডিটিংয়ে আপনার হাত পাকা, বস! আপনার শর্টস ও সোশ্যাল মিডিয়া ক্লিপগুলো দারুণ হচ্ছে।")
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input:
            bot_reply("সাউন্ড সিস্টেম আর 5200/1943 অডিও অ্যাম্প্লিফায়ার নিয়ে আপনার কাজগুলো সত্যিই চমৎকার, বস!")
        elif "স্টক" in user_input or "গ্রো" in user_input or "market" in user_input:
            bot_reply("গ্রো (Groww) অ্যাপে ইনভেস্টিং আর স্টক মার্কেট বা কমোডিটি ট্রেডিং নিয়ে আপনার আপডেটগুলো দারুণ, বস!")
        elif "সাহায্য" in user_input:
            bot_reply("বলুন বস, গেমিং, এডিটিং, ইনভেস্টিং নাকি অন্য কোনো বিষয়ে সাহায্য লাগবে?")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! আবার কথা হবে। ভালো থাকবেন।")
            break
        else:
            bot_reply("বাহ বস, বিষয়টি বেশ ইন্টারেস্টিং! আপনার এই কথাটি আমি মনে রাখছি।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! আমি আপনার এআই চ্যাটবট কিল প্রস্তুত আছি। বলুন, আপনাকে কীভাবে সাহায্য করতে পারি?")

while True:
    try:
        user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কেমন আছেন আপনি?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমি একদম দারুণ আছি, বস! বলুন, আজ আপনার কোডিং বা ক্রিয়েটিভ কাজ কেমন চলছে?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আর আপনি হলেন আমার বস, " + user_name + "!")
        elif "পরিশ্রম" in user_input or "কাজ" in user_input or "দিনমজুরি" in user_input:
            bot_reply("সারাদিন দিনমজুরির কঠিন পরিশ্রমের পর আপনার এই কনটেন্ট ক্রিয়েশনের প্যাশন সত্যিই অনুপ্রেরণাদায়ক, বস!")
        elif "সাবস্ক্রাইবার" in user_input or "চ্যানেল" in user_input or "ইনস্টাগ্রাম" in user_input:
            bot_reply("আপনার ১০০০+ সাবস্ক্রাইবারের মাইলফলক তো কেবল শুরু, বস! সামনে আপনার চ্যানেল আরও অনেক দূর যাবে।")
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input or "ফোন" in user_input:
            bot_reply("Realme 13-এ ফ্রি ফায়ার ম্যাক্স খেলার অভিজ্ঞতা, প্রো লেভেলের সেনসিটিভিটি আর হেডশট টেকনিক একদম ফাটাফাটি, বস!")
        elif "এডিটিং" in user_input or "video editing" in user_input or "ইউটিউব" in user_input:
            bot_reply("কনটেন্ট ক্রিয়েশন এবং ভিডিও এডিটিংয়ে আপনার হাত পাকা, বস! আপনার শর্টস ও সোশ্যাল মিডিয়া ক্লিপগুলো দারুণ হচ্ছে।")
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input:
            bot_reply("সাউন্ড সিস্টেম আর 5200/1943 অডিও অ্যাম্প্লিফায়ার নিয়ে আপনার কাজগুলো সত্যিই চমৎকার, বস!")
        elif "স্টক" in user_input or "গ্রো" in user_input or "market" in user_input:
            bot_reply("গ্রো (Groww) অ্যাপে ইনভেস্টিং আর স্টক মার্কেট বা কমোডিটি ট্রেডিং নিয়ে আপনার আপডেটগুলো দারুণ, বস!")
        elif "সাহায্য" in user_input:
            bot_reply("বলুন বস, গেমিং, এডিটিং, ইনভেস্টিং নাকি অন্য কোনো বিষয়ে সাহায্য লাগবে?")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! আবার কথা হবে। ভালো থাকবেন।")
            break
        else:
            bot_reply("বাহ বস, বিষয়টি বেশ ইন্টারেস্টিং! আপনার এই কথাটি আমি মনে রাখছি।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import openai

# আপনার এআই বটের নাম এবং API Key সেটআপ
bot_name = "কিল"
openai.api_key = "আপনার_এপিআই_কি_এখানে_দিন"

def bot_reply(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "তুমি কিল নামের একজন এআই সহকারী, যে সব সময় বাংলা ভাষায় উত্তর দাও এবং অমিত রবিদাসকে বস বলে সম্বোধন কর।"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return "বসব, নেটওয়ার্ক বা এপিআই-তে একটু সমস্যা হচ্ছে।"

print("🤖 " + bot_name + ": জয় শ্রী রাম, বস! আমি এখন যেকোনো প্রশ্নের উত্তর দিতে প্রস্তুত।")

while True:
    user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
    if user_input.lower() in ["bye", "বিদায়"]:
        print("🤖 " + bot_name + ": জয় শ্রী রাম, বস! ভালো থাকবেন।")
        break
    
    answer = bot_reply(user_input)
    print("🤖 " + bot_name + ": " + answer)
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! জার্ভিস বা ফ্রাইডের স্টাইলে কিল সিস্টেম অনলাইন আছে। বলুন, আজকের মিশন কী?")

while True:
    try:
        user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! সিস্টেম ফুল্লি ফাংশনাল আছে। বলুন, কীভাবে সাহায্য করব?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমার সব সিস্টেম একদম পারফেক্ট আছে, বস! আপনার ক্রিয়েটিভিটি আর কোডিং কেমন চলছে বলুন?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আপনার পার্সোনাল এআই অ্যাসিস্ট্যান্ট এবং বস " + user_name + "-এর ডিজিটাল পার্টনার!")
        elif "স্ট্যাটাস" in user_input or "status" in user_input or "সিস্টেম" in user_input:
            bot_reply("সিস্টেম স্ট্যাটাস: Realme 13 অপ্টিমাইজড, ফ্রি ফায়ার ম্যাক্স কনফিগারেশন রেডি, এবং ভিডিও এডিটিং প্রজেক্ট সিঙ্ক করা আছে, বস!")
        elif "পরিশ্রম" in user_input or "কাজ" in user_input or "দিনমজুরি" in user_input:
            bot_reply("বস, টনি স্টার্কও শূন্য থেকে শুরু করেছিল! আপনার এই কঠোর পরিশ্রম আর কনটেন্ট ক্রিয়েশনের প্যাশন একদিন ইতিহাস গড়বে।")
        elif "সাবস্ক্রাইবার" in user_input or "চ্যানেল" in user_input or "ইনস্টাগ্রাম" in user_input:
            bot_reply("আপনার ১০০০+ সাবস্ক্রাইবারের মাইলফলক তো সবে শুরু, বস! সামনের টার্গেট অর্জনে কিল আপনার সাথেই আছে।")
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input:
            bot_reply("সেনসিটিভিটি এবং হেডশট টেকনিক ফুল প্রো লেভেলে সেট করা আছে, বস! গেমে নামার আগে সিগন্যাল দেবেন।")
        elif "এডিটিং" in user_input or "video editing" in user_input or "ইউটিউব" in user_input:
            bot_reply("ভিডিও ক্লিপস এবং ইউটিউব শর্টসের এডিটিংয়ে আপনার ফিনিশিং সবসময় বস লেভেলের হয়!")
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input:
            bot_reply("5200/1943 অডিও অ্যাম্প্লিফায়ার সার্কিট বোর্ডের কাজ দারুণ এগোচ্ছে, বস! সাউন্ড কোয়ালিটি ফাটাফাটি হবে।")
        elif "স্টক" in user_input or "গ্রো" in user_input or "market" in user_input:
            bot_reply("গ্রো (Groww) অ্যাপের স্টক মার্কেট ও ট্রেডিং ডাটা সিকিউরড আছে, বস!")
        elif "সাহায্য" in user_input:
            bot_reply("বলুন বস, গেমিং, টেক প্রজেক্ট, নাকি কোনো নতুন কোডিং লজিক নিয়ে কাজ করব?")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম অফলাইন হচ্ছে। আবার দেখা হবে।")
            break
        else:
            bot_reply("নির্দেশটি নোট করে নিলাম, বস! ভবিষ্যতে এটি নিয়ে আরও কাজ করব।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! জার্ভিস বা ফ্রাইডের স্টাইলে কিল সিস্টেম অনলাইন আছে। বলুন, আজকের মিশন কী?")

while True:
    try:
        user_input = input("\n✍️ আপনি লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! সিস্টেম ফুল্লি ফাংশনাল আছে। বলুন, কীভাবে সাহায্য করব?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমার সব সিস্টেম একদম পারফেক্ট আছে, বস! আপনার ক্রিয়েটিভিটি আর কোডিং কেমন চলছে বলুন?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আপনার পার্সোনাল এআই অ্যাসিস্ট্যান্ট এবং বস " + user_name + "-এর ডিজিটাল পার্টনার!")
        elif "স্ট্যাটাস" in user_input or "status" in user_input or "সিস্টেম" in user_input:
            bot_reply("সিস্টেম স্ট্যাটাস: Realme 13 অপ্টিমাইজড, ফ্রি ফায়ার ম্যাক্স কনফিগারেশন রেডি, এবং ভিডিও এডিটিং প্রজেক্ট সিঙ্ক করা আছে, বস!")
        elif "পরিশ্রম" in user_input or "কাজ" in user_input or "দিনমজুরি" in user_input:
            bot_reply("বস, টনি স্টার্কও শূন্য থেকে শুরু করেছিল! আপনার এই কঠোর পরিশ্রম আর কনটেন্ট ক্রিয়েশনের প্যাশন একদিন ইতিহাস গড়বে।")
        elif "সাবস্ক্রাইবার" in user_input or "চ্যানেল" in user_input or "ইনস্টাগ্রাম" in user_input:
            bot_reply("আপনার ১০০০+ সাবস্ক্রাইবারের মাইলফলক তো সবে শুরু, বস! সামনের টার্গেট অর্জনে কিল আপনার সাথেই আছে।")
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input:
            bot_reply("সেনসিটিভিটি এবং হেডশট টেকনিক ফুল প্রো লেভেলে সেট করা আছে, বস! গেমে নামার আগে সিগন্যাল দেবেন।")
        elif "এডিটিং" in user_input or "video editing" in user_input or "ইউটিউব" in user_input:
            bot_reply("ভিডিও ক্লিপস এবং ইউটিউব শর্টসের এডিটিংয়ে আপনার ফিনিশিং সবসময় বস লেভেলের হয়!")
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input:
            bot_reply("5200/1943 অডিও অ্যাম্প্লিফায়ার সার্কিট বোর্ডের কাজ দারুণ এগোচ্ছে, বস! সাউন্ড কোয়ালিটি ফাটাফাটি হবে।")
        elif "স্টক" in user_input or "গ্রো" in user_input or "market" in user_input:
            bot_reply("গ্রো (Groww) অ্যাপের স্টক মার্কেট ও ট্রেডিং ডাটা সিকিউরড আছে, বস!")
        elif "সাহায্য" in user_input:
            bot_reply("বলুন বস, গেমিং, টেক প্রজেক্ট, নাকি কোনো নতুন কোডিং লজিক নিয়ে কাজ করব?")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম অফলাইন হচ্ছে। আবার দেখা হবে।")
            break
        else:
            bot_reply("নির্দেশটি নোট করে নিলাম, বস! ভবিষ্যতে এটি নিয়ে আরও কাজ করব।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

# নির্দিষ্ট কিছু এলাকার লোকেশন ও তথ্য ডেটাবেজ
locations_db = {
    "malda": "মালদা, পশ্চিমবঙ্গ - মহানন্দা পল্লী, ইংলিশ বাজার, নিমসরাই এলাকার কাছাকাছি একটি ঐতিহাসিক ও সুন্দর শহর।",
    "english bazar": "ইংলিশ বাজার, মালদা - এটি একটি ব্যস্ত বাণিজ্যিক ও আবাসিক এলাকা।",
    "kolkata": "কলকাতা - পশ্চিমবঙ্গের রাজধানী, যা তার সংস্কৃতি ও ঐতিহ্যের জন্য বিখ্যাত।"
}

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! লোকেশন ও ম্যাপ সিস্টেম অনলাইন আছে। বলুন, কোন জায়গা বা লোকেশন সম্পর্কে জানতে চান?")

while True:
    try:
        user_input = input("\n✍️ জায়গা বা লোকেশনের নাম লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি লিখেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! লোকেশন সিস্টেম অফলাইন হচ্ছে। ভালো থাকবেন।")
            break
        elif "malda" in user_input or "মালদা" in user_input:
            bot_reply("📍 লোকেশন ইনফো: " + locations_db["malda"])
        elif "english bazar" in user_input or "ইংলিশ বাজার" in user_input:
            bot_reply("📍 লোকেশন ইনফো: " + locations_db["english bazar"])
        elif "kolkata" in user_input or "কলকাতা" in user_input:
            bot_reply("📍 লোকেশন ইনফো: " + locations_db["kolkata"])
        else:
            bot_reply(f"বস, '{user_input}' সম্পর্কিত লোকেশন ডেটা আমি নোট করে রাখলাম। এটি গুগল ম্যাপে সার্চ করে দেখে নিতে পারেন!")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

# আপনার যাবতীয় শখ, প্রজেক্ট এবং লাইফস্টাইল ডাটাবেজ
complete_user_database = {
    "profile": "নাম: অমিত রবিদাস (ডাকনাম: শুভ), বয়স: ১৯ বছর, পেশা: দিনমজুরের কঠিন পরিশ্রমের পাশাপাশি ডিজিটাল কনটেন্ট ক্রিয়েটর ও ভিডিও এডিটর।",
    "gaming": "Realme 13 স্মার্টফোনে ফ্রি ফায়ার ম্যাক্স গেম খেলা, প্রো লেভেলের সেনসিটিভিটি এবং হেডশট টেকনিক কনফিগারেশন।",
    "social": "ইউটিউব চ্যানেল (@youtuberboy99999) এবং ১০০০+ সাবস্ক্রাইবারের সফল মাইলফলক অর্জন।",
    "tech_projects": "5200/1943 অডিও অ্যাম্প্লিফায়ার সার্কিট বোর্ড তৈরি এবং স্পিকার সেটআপ নিয়ে কাজ।",
    "finance": "Groww অ্যাপের মাধ্যমে স্টক মার্কেট ও কমোডিটি ট্রেডিং ট্র্যাকিং।"
}

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম ফুল্লি লোডেড এবং অনলাইন আছে। বলুন, আজকের মিশন কী?")

while True:
    try:
        user_input = input("\n✍️ আপনার নির্দেশ লিখুন (বা 'bye' লিখে বের হন): ")
        print("আপনি বলেছেন: " + user_input)
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input or "হ্যালো" in user_input or "হাই" in user_input:
            bot_reply("জয় শ্রী রাম, বস! সিস্টেম পারফেক্টলি কাজ করছে। বলুন, কীভাবে সাহায্য করব?")
        elif "কেমন আছো" in user_input or "how are you" in user_input:
            bot_reply("আমার সব সাব-সিস্টেম একদম ঠিকঠাক আছে, বস! আপনার ক্রিয়েটিভিটি আর কাজ কেমন চলছে বলুন?")
        elif "তোমার নাম কী" in user_input or "who are you" in user_input:
            bot_reply("আমার নাম " + bot_name + ", আপনার পার্সোনাল এআই অ্যাসিস্ট্যান্ট এবং বস " + user_name + "-এর ডিজিটাল পার্টনার!")
        elif "আমার প্রোফাইল" in user_input or "পরিচয়" in user_input:
            bot_reply("বেসিক ইনফো: " + complete_user_database["profile"])
        elif "ফ্রি ফায়ার" in user_input or "free fire" in user_input or "গেম" in user_input:
            bot_reply("গেমিং স্ট্যাটাস: " + complete_user_database["gaming"])
        elif "চ্যানেল" in user_input or "সাবস্ক্রাইবার" in user_input:
            bot_reply("সোশ্যাল মিডিয়া: " + complete_user_database["social"])
        elif "অডিও" in user_input or "অ্যাম্প্লিফায়ার" in user_input:
            bot_reply("টেক প্রজেক্ট: " + complete_user_database["tech_projects"])
        elif "স্টক" in user_input or "গ্রো" in user_input or "market" in user_input:
            bot_reply("ফাইন্যান্স: " + complete_user_database["finance"])
        elif "সব তথ্য" in user_input or "all data" in user_input:
            bot_reply(f"বস, আপনার সমস্ত মেমোরি ডাটা:\n1. {complete_user_database['profile']}\n2. {complete_user_database['gaming']}\n3. {complete_user_database['social']}\n4. {complete_user_database['tech_projects']}\n5. {complete_user_database['finance']}")
        elif "bye" in user_input or "বিদায়" in user_input:
            bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম অফলাইন হচ্ছে। ভালো থাকবেন।")
            break
        else:
            bot_reply("নির্দেশটি নোট করে নিলাম, বস! এটি নিয়ে পরবর্তীতে আরও কাজ করা যাবে।")
                
    except Exception as e:
        print("ত্রুটি দেখা দিয়েছে: ", e)
        break
import speech_recognition as sr

bot_name = "কিল"
user_name = "অমিত রবিদাস"

def bot_reply(text):
    print("🤖 " + bot_name + ": " + text)

# ভয়েস শোনার ফাংশন
def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ শুনছি বলুন, বস...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)
            # বাংলা বা ইংরেজি ভয়েস টেক্সটে রূপান্তর
            text = r.recognize_google(audio, language="bn-BD") 
            print("আপনি মুখে বলেছেন: " + text)
            return text.lower()
        except Exception as e:
            return ""

bot_reply("জয় শ্রী রাম, বস! ভয়েস কমান্ড সিস্টেম রেডি আছে।")

while True:
    user_input = listen_voice()
    
    if user_input == "":
        continue
    
    if "bye" in user_input or "বিদায়" in user_input:
        bot_reply("জয় শ্রী রাম, বস! কিল সিস্টেম অফলাইন হচ্ছে।")
        break
    elif "কেমন আছো" in user_input:
        bot_reply("দম ফাটাফাটি আছে, বস! আপনার ভয়েস কমান্ড একদম ক্লিয়ার শুনছি।")
    else:
        bot_reply(f"আপনার কথাটি নোট করে নিলাম, বস: '{user_input}'")
import os

def create_code_app():
    print("--- আপনার নিজস্ব কোডিং এনভায়রনমেন্ট ---")
    filename = input("ফাইলের নাম দিন (যেমন: my_script.py): ")
    
    print("এবার আপনার কোড লিখুন (শেষ লাইনে 'SAVE' লিখে এন্টার দিন):")
    code_lines = []
    while True:
        line = input()
        if line == "SAVE":
            break
        code_lines.append(line)
        
    # ফাইল সেভ করা
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(code_lines))
        
    print(f"সফল, বস! আপনার কোডটি '{filename}' নামে সেভ হয়ে গেছে।")

create_code_app()
import speech_recognition as sr
import os

def speak(text):
    print("🤖 কিল বলছে: " + text)
    os.system(f"espeak '{text}'")

def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ শুনছি বলুন, বস...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio, language="bn-BD")
            print("আপনি বলেছেন: " + text)
            return text.lower()
        except Exception:
            return ""

speak("জয় শ্রী রাম, বস! ভয়েস সিস্টেম সচল আছে।")

while True:
    command = listen_voice()
    if command == "":
        continue
    
    if "bye" in command or "বিদায়" in command:
        speak("জয় শ্রী রাম, বস! সিস্টেম বন্ধ হচ্ছে।")
        break
    elif "কেমন আছো" in command:
        speak("দম ফাটাফাটি আছি, বস!")
    else:
        speak("আপনার কথাটি বুঝতে পেরেছি, বস।")
import math

def show_profile():
    print("\n--- [1] আমার ব্যক্তিগত প্রোফাইল ---")
    print("নাম: অমিত রবিদাস (ডাকনাম: শুভ)")
    print("বয়স: ১৯ বছর | স্থান: মালদা, পশ্চিমবঙ্গ")
    print("শখ ও কাজ: ইউটিউব কনটেন্ট ক্রিয়েশন, ভিডিও এডিটিং এবং অডিও অ্যাম্প্লিফায়ার প্রজেক্ট।")

def animal_bird_info():
    print("\n--- [2] পশুপাখি ও ফলের তথ্য ---")
    print("🐾 পশুপাখি: বাঘ, হাতি, সিংহ, ঘোড়া, খরগোশ, টিয়া, শালিক, ময়ূর।")
    print("🍎 ফলমূল: আম, কলা, আপেল, কমলা, পেঁপে, আঙুর, লিচু।")

def general_knowledge():
    print("\n--- [3] সাধারণ জ্ঞান ও অন্যান্য তথ্য ---")
    print("🌍 দেশ ও রাজধানী: ভারত (নয়াদিল্লি), বাংলাদেশ (ঢাকা)।")
    print("💻 টেকনোলজি: পাইথন প্রোগ্রামিং, Pydroid 3, অ্যান্ড্রয়েড অ্যাপ ডেভেলপমেন্ট।")

def simple_calculator():
    print("\n--- [4] ক্যালকুলেটর হিসাব ---")
    print("1. যোগ (+)")
    print("2. বিয়োগ (-)")
    print("3. গুণ (*)")
    print("4. ভাগ (/)")
    
    choice = input("হিসাবের ধরন বেছে নিন (1/2/3/4): ")
    
    try:
        num1 = float(input("প্রথম সংখ্যাটি লিখুন: "))
        num2 = float(input("দ্বিতীয় সংখ্যাটি লিখুন: "))
        
        if choice == '1':
            print(f"ফলাফল: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"ফলাফল: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"ফলাফল: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"ফলাফল: {num1} / {num2} = {num1 / num2}")
            else:
                print("ত্রুটি: শূন্য দিয়ে ভাগ করা যায় না!")
        else:
            print("ভুল অপশন সিলেক্ট করেছেন!")
    except ValueError:
        print("দয়া করে সঠিক সংখ্যা লিখুন, বস!")

def main_app():
    print("=========================================")
    print("   জয় শ্রী রাম, বস! অল-ইন-ওয়ান অ্যাপ সচল আছে   ")
    print("=========================================")
    
    while True:
        print("\n--- প্রধান মেনু ---")
        print("1. আমার প্রোফাইল")
        print("2. পশুপাখি ও ফলের তালিকা")
        print("3. সাধারণ জ্ঞান")
        print("4. ক্যালকুলেটর হিসাব")
        print("5. অ্যাপ বন্ধ করুন")
        
        opt = input("\nআপনার পছন্দমতো নম্বরটি লিখুন (1-5): ")
        
        if opt == '1':
            show_profile()
        elif opt == '2':
            animal_bird_info()
        elif opt == '3':
            general_knowledge()
        elif opt == '4':
            simple_calculator()
        elif opt == '5':
            print("\nজয় শ্রী রাম, বস! অ্যাপ বন্ধ হচ্ছে। ভালো থাকবেন।")
            break
        else:
            print("সঠিক নম্বর দিন, বস। আবার চেষ্টা করুন।")

if __name__ == "__main__":
    main_app()
import os

def show_profile():
    print("\n--- ব্যক্তিগত প্রোফাইল ---")
    print("নাম: অমিত রবিদাস (শুভ)")
    print("বয়স: ১৯ বছর")
    print("ঠিকানা: মহানন্দা পল্লী, ইংরেজবাজার, মালদহ")
    print("পেশা: কনটেন্ট ক্রিয়েটর ও টেকনোলজিপ্রেমী")

def show_animals():
    print("\n--- পশুপাখির তালিকা ---")
    print("1. বাঘ (Tiger) - জাতীয় পশু")
    print("2. হাতি (Elephant) - বিশালকায় স্তন্যপায়ী")
    print("3. টিয়া পাখি (Parrot) - কথা বলতে পারে")
    print("4. শালিক (Myna) - চঞ্চল স্বভাবের পাখি")

def show_fruits():
    print("\n--- ফলমূলের তালিকা ---")
    print("1. আম (Mango) - ফলের রাজা (মালদহের আম বিখ্যাত!)")
    print("2. কাঁঠাল (Jackfruit) - জাতীয় ফল")
    print("3. কলা (Banana) - শক্তির উৎস")
    print("4. আপেল (Apple) - পুষ্টিকর ফল")

def calculator():
    print("\n--- সাধারণ ক্যালকুলেটর ---")
    try:
        num1 = float(input("প্রথম সংখ্যাটি লিখুন: "))
        op = input("অপারেটর (+, -, *, /): ")
        num2 = float(input("দ্বিতীয় সংখ্যাটি লিখুন: "))
        
        if op == '+':
            print("ফলাফল:", num1 + num2)
        elif op == '-':
            print("ফলাফল:", num1 - num2)
        elif op == '*':
            print("ফলাফল:", num1 * num2)
        elif op == '/' :
            if num2 != 0:
                print("ফলাফল:", num1 / num2)
            else:
                print("ত্রুটি: শূন্য দিয়ে ভাগ করা যায় না!")
        else:
            print("ভুল অপারেটর!")
    except ValueError:
        print("দয়া করে সঠিক সংখ্যা লিখুন।")

def main():
    while True:
        print("\n================================")
        print("   আমার অল-ইন-ওয়ান ইউটিলিটি অ্যাপ  ")
        print("================================")
        print("1. আমার প্রোফাইল দেখুন")
        print("2. পশুপাখির তালিকা")
        print("3. ফলমূলের তালিকা")
        print("4. ক্যালকুলেটর ব্যবহার করুন")
        print("5. প্রস্থান করুন (Exit)")
        
        choice = input("\nআপনার পছন্দমতো একটি অপশন বেছে নিন (1-5): ")
        
        if choice == '1':
            show_profile()
        elif choice == '2':
            show_animals()
        elif choice == '3':
            show_fruits()
        elif choice == '4':
            calculator()
        elif choice == '5':
            print("\nঅ্যাপটি ব্যবহার করার জন্য ধন্যবাদ, বস! ভালো থাকবেন।")
            break
        else:
            print("\nভুল ইনপুট! দয়া করে ১ থেকে ৫ এর মধ্যে একটি বেছে নিন।")

if __name__ == "__main__":
    main()
def object_analyzer():
    print("\n--- থ্রিডি অবজেক্ট ও ইমেজ অ্যানালাইজার ---")
    print("উপলব্ধ কমান্ডসমূহ:")
    print("1. /cutaway - অবজেক্টের কাট-আওয়ে ভিউ")
    print("2. /explode view - অবজেক্টের ছড়ানো বা এক্সপ্লোডেড ভিউ")
    print("3. /three-sixty view - চারপাশ থেকে ৩৬০ ডিগ্রি ভিউ")
    print("4. /anatomy - অভ্যন্তরীণ গঠন বা অ্যানাটমি বিশ্লেষণ")
    
    cmd = input("\nএকটি কমান্ড বেছে নিন (যেমন: /cutaway): ").strip()
    
    if cmd == "/cutaway":
        print("➡️ প্রসেসিং: অবজেক্টের কাট-আওয়ে ভিউ তৈরি করা হচ্ছে...")
    elif cmd == "/explode view":
        print("➡️ প্রসেসিং: অবজেক্টের বিভিন্ন পার্টস আলাদা করে এক্সপ্লোডেড ভিউ দেখানো হচ্ছে...")
    elif cmd == "/three-sixty view":
        print("➡️ প্রসেসিং: ৩৬০ ডিগ্রি থ্রিডি রোটেশন জেনারেট করা হচ্ছে...")
    elif cmd == "/anatomy":
        print("➡️ প্রসেসিং: ভেতরের স্ট্রাকচার ও অ্যানাটমি স্ক্যান করা হচ্ছে...")
    else:
        print("❌ ভুল কমান্ড! সঠিক কমান্ডটি লিখুন।")
