import appex, ui
import os
from math import ceil, floor

class MachinesView (ui.View):
	...

def main():
	print('Starting')
	
if __name__ == '__main__':
	main()

view = ui.View(frame=(0, 0, 300, 200))
#label = ui.Label(frame=(150, 0, 150, 110), flex='lwh', font=('<System>', 64), alignment=ui.ALIGN_CENTER, name='result_label')
#view.add_subview(label)

appex.set_widget_view(view)


#def roll_action(sender):
#	symbols = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
#	dice = [random.randint(1, 6) for i in range(2)]
#	dice_str = ''.join(symbols[i - 1] for i in dice)
#	sender.superview['result_label'].text = dice_str
	
#v = ui.View(frame=(0, 0, 300, 110))
#label = ui.Label(frame=(150, 0, 150, 110), flex='lwh', font=('<System>', 64), #alignment=ui.ALIGN_CENTER, name='result_label')
#v.add_subview(label)
#button = ui.Button(title='Roll Dice!', font=('<System>', 24), flex='rwh', action=roll_action)
#button.frame = (0, 0, 150, 110)
#v.add_subview(button)


