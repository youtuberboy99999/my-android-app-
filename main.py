from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class PowerfulAIApp(App):
    def build(self):
        # মূল লেআউট
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # স্বাগতম লেবেল
        self.label = Label(
            text='স্বাগতম! আমি আপনার এআই সহকারী।\nভয়েস কমান্ড বা লেখা দিয়ে কাজ করুন।', 
            font_size=18,
            halign='center'
        )
        self.layout.add_widget(self.label)
        
        # ইনপুট বক্স
        self.text_input = TextInput(
            hint_text='এখানে আপনার কমান্ড বা প্রশ্ন লিখুন...', 
            multiline=False,
            size_hint=(1, 0.3)
        )
        self.layout.add_widget(self.text_input)
        
        # প্রসেস বাটন
        self.submit_btn = Button(
            text='কমান্ড রান করুন', 
            size_hint=(1, 0.3),
            background_color=(0.1, 0.6, 0.8, 1)
        )
        self.submit_btn.bind(on_press=self.execute_command)
        self.layout.add_widget(self.submit_btn)
        
        return self.layout

    def execute_command(self, instance):
        user_command = self.text_input.text.lower()
        
        if not user_command:
            self.label.text = 'অনুগ্রহ করে কিছু লিখুন বা বলুন!'
            return

        # মোবাইল বা সিস্টেমের বিভিন্ন কাজের লজিক এখানে যুক্ত হবে
        if 'টাইম' in user_command or 'time' in user_command:
            import time
            current_time = time.strftime('%I:%M %p')
            self.label.text = f'বর্তমান সময়: {current_time}'
            
        elif 'ক্যামেরা' in user_command or 'photo' in user_command:
            self.label.text = 'ক্যামেরা সার্ভিস চালু করা হচ্ছে...'
            # এখানে অ্যান্ড্রয়েড ক্যামেরা খোলার কোড বা ইন্টিগ্রেশন বসবে
            
        elif 'ক্যালকুলেটর' in user_command:
            self.label.text = 'ক্যালকুলেটর ফিচার ওপেন করা হচ্ছে...'
            
        else:
            self.label.text = f'এআই উত্তর: আপনি "{user_command}" বলেছেন। এটি নিয়ে কাজ চলছে।'

if __name__ == '__main__':
    PowerfulAIApp().run()
  
