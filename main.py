from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

class SplashScreen(BoxLayout):
    def __init__(self, switch_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.spacing = 10
        self.switch_callback = switch_callback

        # logo + title
        self.add_widget(Image(source='icon.png'))
        self.add_widget(Label(
            text="anigye kojo amenlemah's robotics project (mental math duel)",
            font_size=22,
            halign="center"
        ))
        # After ~3 seconds, go to game
        Clock.schedule_once(lambda dt: self.switch_callback(), 3)

class MathGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.score1 = 0
        self.score2 = 0
        self.rounds = 0
        self.max_rounds = 5
        self.current_player = 1
        self.timer = 10
        self.timer_event = None

        self.question_label = Label(text="Press Start to begin", font_size=24)
        self.add_widget(self.question_label)

        self.score_label = Label(text="Player 1: 0 | Player 2: 0", font_size=20)
        self.add_widget(self.score_label)

        self.timer_label = Label(text="Time left: 10", font_size=18)
        self.add_widget(self.timer_label)

        # auto-start after splash for demo; swap for a Button if you want manual start
        self.add_widget(Label(text="[ starting… ]", font_size=18))
        Clock.schedule_once(lambda dt: self.start_game(None), 1)

    def start_game(self, _):
        self.score1 = 0
        self.score2 = 0
        self.rounds = 0
        self.next_round()

    def next_round(self, *args):
        if self.rounds >= self.max_rounds:
            self.end_game()
            return

        self.rounds += 1
        self.current_player = 1 if self.rounds % 2 != 0 else 2
        self.num1 = random.randint(1, 10 * self.rounds)
        self.num2 = random.randint(1, 10 * self.rounds)
        self.answer = self.num1 + self.num2

        self.question_label.text = f"Player {self.current_player}, what is {self.num1} + {self.num2}?"
        self.start_timer()

    def start_timer(self):
        self.timer = 10
        self.timer_label.text = f"Time left: {self.timer}"
        if self.timer_event:
            self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.timer -= 1
        self.timer_label.text = f"Time left: {self.timer}"
        if self.timer <= 0:
            self.timer_event.cancel()
            self.check_answer(None)

    def check_answer(self, _):
        # simple demo logic; replace with TextInput/Button UI to collect answers
        correct = random.choice([True, False])
        if correct:
            if self.current_player == 1:
                self.score1 += 1
            else:
                self.score2 += 1

        self.score_label.text = f"Player 1: {self.score1} | Player 2: {self.score2}"
        self.next_round()

    def end_game(self):
        if self.score1 > self.score2:
            winner = "Player 1"
        elif self.score2 > self.score1:
            winner = "Player 2"
        else:
            winner = "No one"
        Popup(
            title="Game Over",
            content=Label(
                text=f"🎉 {winner} is the Champion!\nMake sure you won or Sir Kwame's shiny head will blind you"
            ),
            size_hint=(0.85, 0.45)
        ).open()

class MathApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='vertical')
        self.show_splash()
        return self.root_layout

    def show_splash(self):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(SplashScreen(self.show_game))

    def show_game(self, *args):
        self.root_layout.clear_widgets()
        self.root_layout.add_widget(MathGame())

if __name__ == '__main__':
    MathApp().run()