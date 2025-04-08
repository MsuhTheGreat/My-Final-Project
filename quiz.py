import requests
import tkinter as tk
import random
import html
import time
from dotenv import load_dotenv
import os


BACKGROUND_COLOR = "#B1DDC6"
TICK_IMAGE_PATH = "final_project\\images\\tick.png"
CROSS_IMAGE_PATH = "final_project\\images\\cross.png"
SHARP_TICK_IMAGE_PATH = "final_project\\images\\tick_darkened.png"
SHARP_CROSS_IMAGE_PATH = "final_project\\images\\cross_darkened.png"
QUIZ_WINDOW_BACKFROUND_IMAGE_PATH = "final_project\\images\\background.png"
TOKENS_ENV_PATH = "final_project\\tokens.env"
OPEN_TRIVIA_DATABASE_URL = "https://opentdb.com/api.php"
# load_dotenv(TOKENS_ENV_PATH)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")



class Quiz:
    
    def __init__(self, window:tk.Tk) -> None:
        self.score_value = 0
        self.questions_answered = 0
        self.questions = self.get_questions()
        
        self.window = window
        self.window.title("Quiz Window")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.question_background_pic = tk.PhotoImage(file=QUIZ_WINDOW_BACKFROUND_IMAGE_PATH)
        self.tick_mark_image = tk.PhotoImage(file=TICK_IMAGE_PATH)
        self.cross_mark_image = tk.PhotoImage(file=CROSS_IMAGE_PATH)
        self.sharp_tick_image = tk.PhotoImage(file=SHARP_TICK_IMAGE_PATH)
        self.sharp_cross_image = tk.PhotoImage(file=SHARP_CROSS_IMAGE_PATH)
        
        self.score = tk.Label(self.window, text="Score: 0", font=("Arial", 40, "normal"), highlightthickness=0, bg=BACKGROUND_COLOR, pady=20)
        self.score.grid(row=0, column=1)

        self.canvas = tk.Canvas(self.window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.pic = self.canvas.create_image(400, 263, image=self.question_background_pic)
        # self.score = self.canvas.create_text(400, 150, text="Score: 0", font=("Arial", 40, "normal"))
        self.question = self.canvas.create_text(400, 263, text="Question", font=("Arial", 40, "italic"), width=500)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.pic = self.question_background_pic

        self.tick_button = tk.Button(self.window, image=self.tick_mark_image, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=self.clicked_tick)
        self.tick_button.grid(row=2, column=1)
        self.tick_button.pic = self.tick_mark_image

        self.cross_button = tk.Button(self.window, image=self.cross_mark_image, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=self.clicked_cross)
        self.cross_button.grid(row=2, column=0)
        self.cross_button.pic = self.cross_mark_image

        self.load_question()

    
    def answer_is_right(self, user_answer):
        question_dict = self.questions[self.questions_answered]
        return (user_answer == question_dict["answer"])

    
    def clicked_tick(self):
        if self.questions_answered <= len(self.questions):
            if self.answer_is_right("True"):
                self.score_value += 1
                self.show_tick()
            else:
                self.show_cross()
            self.questions_answered += 1
            self.load_question()
    

    def clicked_cross(self):
        if self.questions_answered <= len(self.questions):
            if self.answer_is_right("False"):
                self.score_value += 1
                self.show_cross()
            else:
                self.show_tick()
            self.questions_answered += 1
            self.load_question()
    

    def show_tick(self):
        # self.deactivate_buttons()
        self.tick_button.config(image=self.sharp_tick_image)
        self.tick_button.pic = self.sharp_tick_image
        self.window.after(1000, self.restore_defaults)
    

    def show_cross(self):
        # self.deactivate_buttons()
        self.cross_button.config(image=self.sharp_cross_image)
        self.cross_button.pic = self.sharp_cross_image
        self.window.after(1000, self.restore_defaults)
    

    def restore_defaults(self):
        self.tick_button.config(image=self.tick_mark_image)
        self.tick_button.pic = self.tick_mark_image
        self.cross_button.config(image=self.cross_mark_image)
        self.cross_button.pic = self.cross_mark_image
        # self.activate_buttons()

    
    # def activate_buttons(self):
    #     self.tick_button.config(state="normal")
    #     self.cross_button.config(state="normal")
    
    
    # def deactivate_buttons(self):
    #     self.tick_button.config(state="disabled")
    #     self.cross_button.config(state="disabled")
    #     self.window.after(1500, self.restore_defaults)


    def reset_token(self):
        reset_url = f"https://opentdb.com/api_token.php?command=reset&token={ACCESS_TOKEN}"
        response = requests.get(reset_url)
        response.raise_for_status()
        print(response.text)
    
    
    def get_questions(self):
        questions = []
        amount_for_each = 5
        
        catagories = [
            {"name":"Science & Nature", "id": 17},
            # {"name":"General Knowledge", "id": 9},
        ]
        
        for catagory in catagories:
            wait = False
            if len(catagories) == 1:
                wait = True
            parameters = {
                # "amount": amount_for_each,
                "amount": 10,
                "type": "boolean",
                "difficulty": "easy",
                # "category": catagory["id"],
                "token": ACCESS_TOKEN
            }
            
            response = requests.get(url=OPEN_TRIVIA_DATABASE_URL, params=parameters)
            response.raise_for_status()
            data = response.json()
            
            if int(data["response_code"]) == 4:
                time.sleep(4)
                self.reset_token()
                continue
            
            question_data = data["results"]
            questions.extend(
                {
                    "question": html.unescape(item["question"]),
                    "answer": html.unescape(item["correct_answer"])
                }
                for item in question_data
            )
            
            if not wait:
                time.sleep(4)
                wait = True
        
        random.shuffle(questions)
        return questions


    def load_question(self):
        self.score.config(text=f"Score: {self.score_value}")
        if self.questions_answered < len(self.questions):
            question_dict = self.questions[self.questions_answered]
            text = f"Q{self.questions_answered + 1}. {question_dict['question']}"
            self.canvas.itemconfig(self.question, text=text)
        else:
            self.window.after(1000, self.end_quiz)


    def end_quiz(self):
        self.canvas.itemconfig(self.question, text="Quiz Completed! 🎉")
        self.tick_button.config(state="disabled")
        self.cross_button.config(state="disabled")
        self.window.after(2000, self.window.destroy)
                


if __name__ == "__main__":
    window = tk.Tk()
    Quiz(window)
    window.mainloop()