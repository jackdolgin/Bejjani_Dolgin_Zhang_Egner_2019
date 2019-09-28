#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Author: Jack Dolgin, 01/2019 '''

from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
import numpy as np                                                              # Whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os                                                                       # Handy system and path functions
import sys                                                                      # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = (os.path.dirname(
            os.path.abspath(__file__)).decode(sys.getfilesystemencoding()))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'PDR_script'                                                          # From the Builder filename that created this script
expInfo = {'participant':'','session':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()                                                                 # User pressed cancel during popout
expInfo['date'] = data.getDateStr()                                             # Add a simple timestamp
expInfo['expName'] = expName

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, allowGUI=False,
    monitor='testMonitor', color=[1,1,1], useFBO=True)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()

# cueversions = np.repeat([0,1,2,3,4,5],4)                                      # Randomizes assignment of cues for participants, counterbalanced, counterbalanced
# np.random.shuffle(cueversions)                                                # We ran this script with this line and the above line once, used the output to create the lists directly below, and then commented this line out

if int(expInfo['session']) == 1:
    cueversions = [3,0,3,3,2,3,1,4,2,5,0,5,4,2,5,1,0,4,2,5,4,1,0,1,5.0,1,3,2,4,
                  2,5,4,2,5,3,0,3,1,2,5,4,5,1,5,4,4,2,3,0,4,1,2,0,3,5,3,5,2,1,
                  4,0,3,1,0,0,1]
elif int(expInfo['session']) == 2:
    cueversions = [1,2,5,4,1,5,4,0,0,1,4,4,0,2,3,2,3,3,5,1,0,5,3,2,1,3,5,4,0,2,
                   0,2,4,1,3,5,3,4,0,1,2,1,4,0,3,4,2,1,5,1,3,5,0,3,5,4,2,1,3,0,
                   5,2,1,4,4,3,5,0,2,1,5,1,4,3,0,2,1,4,3,5,2,1,0,1,2,3,4,5,0,1]
elif int(expInfo['session']) == 3:
    cueversions = [4,4,4,4,2,5,0,1,5,5,1,4,3,0,2,4,1,3,3,1,3,2,0,0,5,2,3,4,0,1,
                   3,4,2,5,2,1,3,3,5,4,1,4,2,3,0,5,1,0,2,4,0,5,0,1,3]
elif int(expInfo['session']) == 4:
    cueversions = [1,2,2,2,3,3,4,5,1,5,0,0,2,0,0,4,1,3,3,5,4,5,4,1,0,2,4,4,1,3,
                   5,4,2,3,1,0,0,0,0,1,3,5,4,3,0,2,1,5,1,2,0,4,3,4,3,0,2,5,1]

CueVersion = cueversions[int(expInfo['participant'])%100 - 1]

expInfo['cueVersion'] = CueVersion                                              # Saves cue version in eventual csv

filename = (_thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'],     # Creates csv name as participant number + 'PDR_script' + experiment number
           expName, "ses_" + expInfo['session']))

thisExp = data.ExperimentHandler(name=expName, version='',                      # An ExperimentHandler isn't essential but helps with data saving
    extraInfo=expInfo, dataFileName=filename)

logFile = logging.LogFile(filename+'.log', level=logging.EXP)                   # Save a log file for detail verbose info
logging.console.setLevel(logging.WARNING)                                       # This outputs to the screen, not a file




##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##
##-----------------------------START CODE-------------------------------------##
##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##



##----------------------------------------------------------------------------##
##--------------------------SET UP STIMULI------------------------------------##
##----------------------------------------------------------------------------##


##--------------------------SET UP TEXT & CUES--------------------------------##

lowvowelSet = ['a','e','i','o','u']                                             # Note: all vowels and both their cases are used as stimuli
capvowelSet = ['A','E','I','O','U']
lowconsonantSet = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s', # Note: all consonants and both their cases are used as stimuli
                   't','v','w','x','y','z']
capconsonantSet = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S',
                   'T','V','W','X','Y','Z']
instr_letters = ['O','o','K','k','U','u','S','s','C','c','W','w','Z','z','V',   # Each of these letters was presented once to every participant during a pseudo-practice session; the session was for learning the different appearances between uppercase and lowercase
                 'v','X','x']

cuelist = [[2,4,8,],[2,8,4],[4,2,8],[4,8,2],[8,2,4],[8,4,2]]                    # Permutations of three numbers and their assigned cues
cueSet = cuelist[CueVersion]                                                    # Selects the participant's randomly-assigned cue permutation
cueA = cueSet[0]                                                                # Cue number for predictive switch
cueB = cueSet[1]                                                                # Cue number that's non-predictive
cueC = cueSet[2]                                                                # Cue number for predictive repeat


##------------------------INSTRUCTION SCREEN----------------------------------##

Instr_1a = visual.TextStim(win=win, name='Instr_1a', color='black',
    text = ('Please read these instructions carefully before you begin the '
           'experiment. Press the spacebar to continue.'))

Instr_1b = visual.TextStim(win=win, name='Instr_1b', color='black',
    text = ('We are interested in how participants process demands on their '
           'attention. In this experiment, you will be asked to judge whether '
           'a letter is a CONSONANT or VOWEL or whether a letter is in '
           'UPPERCASE or LOWERCASE.'))

cueAinstr = (str(cueA) + '") will precede trials in which the letter judgment '
             '(consonant/vowel vs. uppercase/ lowercase) will switch from that '
             'of the previous trial.')

cueBinstr = (str(cueB) + '") will precede trials in which the letter judgment '
             'will either switch or remain the same from the previous trial. '
             'You may use this information to aid your performance.')

cueCinstr = (str(cueC) + '") will precede trials in which the letter judgment '
             'will remain the same as in the previous trial.')

# Whether expt 1 + 2 or 3 + 4 determines whether instructions mention a mask (since in 3 + 4 there is no mask), as well as whether trial 250 is the end of the experiment or whether there is also a cue-perception task
if int(expInfo['session']) < 3:

    Instr_1c = visual.TextStim(win=win, name='Instr_1c', color='black',
        text = ('On each trial, a pattern of five Xs will appear on-screen '
              'followed by a letter that you will categorize according to the '
              'color of its surrounding rectangle. The Xs are not relevant to '
              'the task that you are performing.'))

    Instr_1c_2 = visual.TextStim(win=win, name='Instr_1c_2', color='black',     # this Instr_1c_2 will only display for exp 2
        text = ('However, before the Xs are presented, number cues will flash '
               'on-screen. One of these cues ("' + cueAinstr))

    Instr_1c_3 = visual.TextStim(win=win, name='Instr_1c_3', color='black',     # this Instr_1c_3 will only display for exp 2
        text = ('One of the cues ("' + cueCinstr + ' One of the cues "('
                +  cueBinstr))

    Ending = visual.TextStim(win=win, name='End', color='black',
        text = ('You have finished the experiment! Please press spacebar to '
               'close out and let the experimenter know you\'re ready for the '
               'demographic survey.'))

else:

    Instr_1c = visual.TextStim(win=win, name='Instr_1c', color='black',
        text = ('On each trial, a number cue will appear on-screen followed by '
               'a letter that you will categorize according to the color of '
               'its surrounding rectangle.'))

    Instr_1c_2 = visual.TextStim(win=win, name='Instr_1c_2', color='black',     # this Instr_1c_2 will only display for exp 4
        text = ('One of these cues ("' + cueAinstr + ' One of the cues ("'
                + cueCinstr))

    Instr_1c_3 = visual.TextStim(win=win, name='Instr_1c_3', color='black',     # this Instr_1c_3 will only display for exp 4
        text = 'One of the cues ("' + cueBinstr)

    Ending = visual.TextStim(win=win, name='End', color='black',
        text = ('You have finished the main part of the experiment! Please '
                'press spacebar to close out and let the experimenter know '
                'you\'re ready for the post-test.'))

Instr_1d = visual.TextStim(win=win, name='Instr_1d', color='black',
    text = ('If the rectangle is blue, discriminate between vowel and '
            'consonant. Press the z/Z key to categorize the letter as a vowel '
            'and the 3 key on the numpad if it is a consonant.'))

Instr_1e = visual.TextStim(win=win, name='Instr_1e', color='black',
    text= ('If the rectangle is green, discriminate between lowercase and '
           'uppercase. Press the z/Z key if the letter is lowercase/small and '
           'the 3 key on the numpad if it is uppercase.'))

Instr_1f = visual.TextStim(win=win, name='Instr_1f', color='black',
    text = ('Respond to each letter stimulus as quickly as possible while '
            'still being accurate. In the beginning of the task, the letter '
            'will stay on-screen until you make your response, but this will '
            'change later in the task. Always press the z key with your LEFT '
            'index finger and the 3 key on the numpad with your RIGHT index '
            'finger.'))

Instr_1g = visual.TextStim(win=win, name='Instr_1g', color='black',
    text = ('It is very important to stay focused during the experiment. '
            'Please respond accurately.'))

Instr_1h = visual.TextStim(win=win, name='Instr_1h', color='black',
    text = ('Performance feedback is provided. You will hear a '
            'high-frequency tone if you respond correctly and a low-frequency '
            'tone if you respond incorrectly. To give you a visualization of '
            'the task, press the spacebar to move on to the next page.'))

Mapping = visual.ImageStim(win=win, name='Mapping',                             # Loads image mapping responses to keys
    image = os.path.join('stimuli','Mapping.png'), size=(1,2))

Instr_1i = visual.TextStim(win=win, name='Instr_1i', color='black',
    text = ('Since you will be asked to distinguish between uppercase and '
            'lowercase in some trials, some sample letters will be presented '
            'to get you familiar with the font size. Press the spacebar '
            'to continue.'))

Instr_1j = visual.TextStim(win=win, name='Instr_1j', color='black',
    text = ('To get acclimated with the demands of each task, you will start '
           'with some practice trials. Press the spacebar when you are ready '
           'to start the practice trials.'))

Instr1 = visual.TextStim(win=win, name='Instr1', color='black',
    text = ('You have finished the practice trials and you accurately '
           'answered $str(corrP) trials. The experiment starts now. '
           'Press the spacebar to continue.'))

Instr_1k = visual.TextStim(win=win, name='Instr_1k', color='black',
    text = 'Press the spacebar to start the main experiment.')

Instr_2a = visual.TextStim(win=win, name='Instr_2a',color='black',
    text = ('From now on, it is important to respond both accurately and '
           'quickly. Accurate but slow responses are now counted as incorrect '
           'trials. Please adjust the speed of your responses according to the '
           'performance feedback you receive. Press the spacebar to continue.'))

Instr_2b = visual.TextStim(win=win, name='Instr_2b',color='black',
    text = 'As a reminder, ("' + cueAinstr + ' ("' + cueCinstr)

Instr_2c = visual.TextStim(win=win, name='Instr_2c', color='black',
    text = '("' + cueBinstr)

InstrText = visual.TextStim(win=win, name='InstrText', color='black',
    text = 'default text', pos=(0, 0.5))

CueTestA = visual.TextStim(win=win, name='CueTest', color='black',
    text = 'Press the number associated with only task-switch (hard) trials.',)

CueTestB = visual.TextStim(win=win, name='CueTest', color='black',
    text = 'Press the number unpredictive of the upcoming trial (neutral).')

CueTestC = visual.TextStim(win=win, name='CueTest', color='black',
    text = 'Press the number associated with only task-repeat (easy) trials.')

CueTest_list = [[CueTestA, cueA], [CueTestB, cueB], [CueTestC, cueC]]           # matches the cue probe question with the correct response; the order of the list of lists get randomized every time they're presented

Instr_probe_miss = visual.TextStim(win=win, name='Instr_probe_miss',
    color='black', text = ('You answered at least one of the three '
                            'cue-related questions incorrectly. Please '
                            'press the spacebar to try again.'))

Post_Instr_1 = visual.TextStim(win=win, name='Post_Instr_1', color='black',
    text = ('Welcome to the post-test! You will answer a few questions about '
           'the experimental stimuli and do some judgement tasks. Press the '
           'spacebar to continue.'))

Post_Instr_2 = ('In this session, a letter, digit, or symbol will be '
'presented, before the 5 Xs. If you can see or guess its identity, press '
'the corresponding key (e.g., if you see 7, press 7; if you see '
'\'b\', press b). If you did not see anything and cannot '
'guess, then press enter. There is no time limit to respond if '
'are uncertain about your response. Press the spacebar to begin.')

Post_Q1 = visual.TextStim(win=win, name='Post_Q1', color='black',
    text = ('Did you notice anything being briefly presented before the 5 Xs '
            'in each trial? Press Y if you noticed and N if you did not.'))

Post_Q2 = visual.TextStim(win=win, name='Post_Q2', color='black',
    text = ('Were you aware of the identity of this brief stimulus? Press Y if '
            'you were and N if you were not.'))

Post_Q3 = visual.TextStim(win=win, name='Post_Q3', color='black',
    text = ('What is the identity of this brief stimulus presented before the '
            '5 Xs? If it is a number, press N; If it is a symbol, press S; If '
            'it is a letter, press L. Even if you are not explicitly aware of '
            'the stimulus, you are still encouraged to guess.'))


##-------------------------------SHAPES---------------------------------------##

Cue = visual.TextStim(win=win, name='Cue', color='black', text='default text')

Mask = visual.ImageStim(win=win, name='Mask',
    image = os.path.join('stimuli','Mask.png'),
    size=(0.42, 0.5), interpolate = True)

StimLetter = visual.TextStim(win=win, name='StimLetter', text='default text',
                             color='black')

polygon = visual.Rect( win=win, name='polygon', lineWidth=8, lineColor=1.0)

Fixation = visual.TextStim(win=win, name='Fixation', color='black', text='+')


##------------------------LOAD SOUND NOISE & SET VOLUME-----------------------##

sound_clip = sound.Sound('A', secs=-1)
sound_clip.setVolume(1)
soundfiles = [os.path.join('stimuli','ding.wav'),
              os.path.join('stimuli','chord.wav')]


##-------------------------INTERVALS & DURATION SIZES-------------------------##

framelength = win.monitorFramePeriod
def to_frames(t):                                                               # Converts time to frames accounting for the computer's refresh rate (aka framelength); input is the desired time on screen, but the ouput is the closest multiple of the refresh rate
    return int(round(t / framelength))

ITI_min = to_frames(2)                                                          # Minimum inter-trial duration (for randomization)
ITI_max = to_frames(3)                                                          # Maximum inter-trial duration (for randomization)
cue_duration = to_frames(.0117)                                                 # Duration that cue is on screen (in sec)
mask_delay = to_frames(.0232)                                                   # Delay between cue and mask (in sec)
if int(expInfo['session']) < 3:                                                 # For exps 1 and 2 set mask duration as .5 sec, otherwise set mask duration as 0 (meaning the mask doesn't appear )
    mask_duration = to_frames(.5)
else:
    mask_duration = 0
stim_delay_min = to_frames(1.5)                                                 # Minimum delay between mask and stimlus (for randomization)
stim_delay_max = to_frames(2.5)                                                 # Maximum delay between mask and stimlus (for randomization)


##--------------------------------CREATE TIMERS-------------------------------##

globalClock = core.MonotonicClock()                                             # To track the time since experiment started
trialClock = core.Clock()                                                       # Unlike globalclock, gets reset each trial


##---------------------------TRIAL MATRIX & RANDOMIZATION---------------------##

SRmapping_full = ['z', 'num_3']                                                 # `num_3` corresponds to the 3 located only on the numeric keypad
taskColorRGB = ["#0000ff","#00ff00"]                                            # blue, green

ptrials = 12                                                                    # Number of practice trials
maintrials = 250                                                                # Number of main experimental trials
switchfreq = .25                                                                # Percent of trials that are switches
switchtrials = int(np.floor(maintrials*switchfreq))                             # Number of switch trials
repeattrials = maintrials - switchtrials                                        # Number of repeat trials
posttrials = 30                                                                 # Number of trials at the end testing subliminal perception
extra_appearances = ([1,1,0,0])                                                 # Although we try to include an equal number of uppercase vowel, uppercase consonant, lowercase vowel, and lowercase consonant trials, 250%4=2, so this line randomly distributes each of the two 'extra' trials to one of these letter types

def expmatrix(trials):
    Cue = ([cueA]*int(round(trials*.25*.5)) + [cueB]*int(round(trials*.5))      # Sets the predictive switch cue for half of switch trials, the non-predictive cue for the other half of switch and half of repeat trials,
           + [cueC]*int(round(trials*.75*.5)))                                  # and the predictive repeat cue for the other half of repeat trials

    if trials == ptrials:
        continuity = (['repeat']*int((trials/2)) + ['switch']                   # This and the next two lines set the first half of practice trials as 'vowel/consonant' trials
                     + ['repeat']*int((trials/2) - 1))                          # and the second half as 'upper/lowercase' trials
        currentTask = 1
    elif trials == maintrials:

        continuity = ['switch']*switchtrials + ['repeat']*repeattrials          # Sets 25% (62/250) of trials as switch trials and 75% as repeat trials
        currentTask = random.choice([1,2])                                      # Randomizes the task for the first trial in the main exp; starting point for the `continuity` list that determines the task for each trial
        toshuffle = list(zip(continuity, Cue))                                  # This and next two lines shuffle the order of repeat/switch trials and their corresponding cues
        random.shuffle(toshuffle)
        continuity[:], Cue[:] = zip (*toshuffle)                                # "zip" means we can randomize cues and switch/repeats in the same order so cues still appear with only certain trial types

    np.random.shuffle(lowvowelSet)                                              # Randomize list order of lowercase vowels
    np.random.shuffle(capvowelSet)                                              #                         uppercase vowels
    np.random.shuffle(lowconsonantSet)                                          #                         lowercase consonants
    np.random.shuffle(capconsonantSet)                                          #                         uppercase consonants
    np.random.shuffle(extra_appearances)

    # Sets an equal number of trials in both practice and main experimente that are uppercase vowel, uppercase consonant, lowercase vowel, and lowercase consonant trials
    if trials == ptrials:
        stimSet = (lowconsonantSet[:3] + capconsonantSet[:3]
                  + lowvowelSet[:3] + capvowelSet[:3])
    elif trials == maintrials:
        stimSet = (lowconsonantSet*2 + capconsonantSet*2 + lowvowelSet*12
                   + capvowelSet*12 + lowconsonantSet[0+extra_appearances[0]:]
                   + capconsonantSet[0+extra_appearances[1]:]
                   + lowvowelSet[2 + extra_appearances[2]:]
                   + capvowelSet[2 + extra_appearances[3]:])

    np.random.shuffle(stimSet)                                                  # Randomize trial order of letter types

    task = []
    corrAns = []
    taskColor = []
    ITI = []
    stim_delay = []

    for tr in range(len(continuity)):
        # Determines which task to present depending on whether it's a switch or repeat trial, and appends this task to the experimental matrix
        if continuity[tr] == 'repeat':
            task.append(currentTask)
        else:
            task.append(3-currentTask)                                          # We use "3-" because 3-2 = 1 and 3-1=2, representing the two tasks' numbers
        currentTask = task[tr]

        if ((currentTask == 1 and stimSet[tr] in (lowvowelSet + capvowelSet))   # If it's a vowel/consonant trial and the stimulus is a vowel,
           or (currentTask == 2 and stimSet[tr].islower())):                    # or it's a upper/lowercase trial and the stimulus is lowercase,
            corrAns.append(SRmapping_full[0])                                   # Set the correct response as "z" and append this response to the experimental matrix
        else:                                                                   # otherwise set the correct response as the keypad  number 3 button
            corrAns.append(SRmapping_full[1])

        # append the task type and corresponding rectangle color to the experimental matrix
        if currentTask == 1:
            task[tr] = 'vowel/consonant'                                        # replaces the number representing task with the string corresponding to that number
            taskColor.append(taskColorRGB[0])
        else:
            task[tr] = 'vowel/consonant'
            taskColor.append(taskColorRGB[1])
        ITI.append(random.randint(ITI_min, ITI_max))                            # Append the randomized ITI (jittered between 2000-3000 ms) to the experimental matrix
        stim_delay.append(random.randint(stim_delay_min, stim_delay_max))       # Append the randomized delay between mask and stimulus (jittered between 1500-2500 ms) to the experimental matrixx

    return [stimSet, continuity, task, taskColor, corrAns, Cue,
            ITI, stim_delay]

postCues = np.repeat(cueSet, posttrials/len(cueSet))                            # Repeat each of the three cues 10 times
np.random.shuffle(postCues)                                                     # Shuffle the order of these 30 cues
postmatrix = [postCues, [random.randint(ITI_min, ITI_max) for i in range(posttrials)]] # Creates an experimental matrix for the cue perception post-task (only relevant for exps 1 + 2); matrix includes only the 30 randomized cues and randomized ITI's



##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##
##--------------------------START RUNNING TRIALS------------------------------##
##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##



##----------------------------------------------------------------------------##
##---------------------------START INSTRUCTIONS-------------------------------##
##----------------------------------------------------------------------------##



instr_list = [Instr_1a, Instr_1b, Instr_1c, Instr_1c_2, Instr_1c_3, Instr_1d,
              Instr_1e, Instr_1f, Instr_1g, Instr_1h, Mapping, Instr_1i]

for instr in range(len(instr_list)):
    if instr not in range(3,5) or int(expInfo['session']) % 2 == 0:             # For experiments 2 + 4 loop through all the instructions; for experiments 1 + 3 loop through all instructions except the screens with cue information
        instr_list[instr].setAutoDraw(True)
        while len(event.getKeys(keyList=["space"])) == 0:                       # Proceed to next instruction when spacebar is pressed
            win.flip()
        instr_list[instr].setAutoDraw(False)


##-------------------------START PSEUDO-PRACTICE------------------------------##

for trial in range(len(instr_letters)):
    StimLetter.setText(instr_letters[trial])                                    # Set/update letter to display

    # alternate between uppercase and lowercase letters
    if trial%2 == 0:
        taskColorinstr = taskColorRGB[random.choice([0,1])]
        textinstr = "This is an uppercase."
    else:
        textinstr = "This is a lowercase."

    polygon.setLineColor(taskColorinstr)                                        # Set/update colored rectangle
    InstrText.setText(textinstr)                                                # Set/update 'This is a(n) upper/lowercase.' text
    [a_stim.setAutoDraw(True) for a_stim in [InstrText, polygon, StimLetter]]   # Display text, stimulus, and rectangle...
    while len(event.getKeys(keyList=['space'])) == 0:                           # ...until participant presses spacebar
        win.flip()

[a_stim.setAutoDraw(False) for a_stim in [InstrText, polygon, StimLetter]]
Instr_1j.setAutoDraw(True)                                                      # Display one final instruction screen before practice trials
while len(event.getKeys(keyList=['space'])) == 0:
    win.flip()
Instr_1j.setAutoDraw(False)



##----------------------------------------------------------------------------##
##-----------------------------START TRIALS-----------------------------------##
##----------------------------------------------------------------------------##


corrP = 0                                                                       # Starting counter for number of practice trials participants answer correctly, which is then displayed to them as feedback before the main experiment begins
trialcounter = -ptrials                                                         # Results in the practice trials having a negative trial number and the first experimental trial being trial 0
trialmatrix = expmatrix(ptrials)                                                # Sets initial trial matrix corresponding to the practice trials, and is then replaced by the trials in main experiment when we loop through rep > 0
trials = range(ptrials)                                                         # Sets initial number of trials equal to the practice trials, and is then replaced by the trials in main experiment when we loop through rep > 0
for rep in range(5 - (int(expInfo['session']))/3):                              # "5 - ..." indicates that there's a fifth item (the cue-perception task) in the loop to iterate though for experiments 1 + 2


    ##--------------------------START MAIN EXPERIMENT-------------------------##

    if rep > 0:
        trialmatrix = expmatrix(maintrials)
        if rep == 1:
            if int(expInfo['session']) % 2 == 0:
                next = 'continue.'
            else:
                next = 'begin the main experiment.'
            Instr1.setText('Your accuracy on the practice task was '
                          + str(corrP) + ' out of 12. If you are confused '
                          'about the response keys for each task, please '
                          'call over the experimenter. Press the spacebar '
                          'to ' + next)
            Instr1.setAutoDraw(True)
            while len(event.getKeys(keyList=['space'])) == 0:                   # Pressing space advances through the practice feedback screen
                win.flip()
            Instr1.setAutoDraw(False)
            trials = range(50)                                                  # Sets up the first 50 experimental trials to be for-looped
        elif rep < 4:
            rt_thresh = float(np.percentile(RTF, 60, interpolation = 'nearest'))/framelength # Calculates RT cutoff for the upcoming rep based on the 60th percentile of correct, repeat trials from the previous rep
            if rep == 2:
                Instr_2a.setAutoDraw(True)                                      # Informs participants they must respond quickly on upcoming trials; presented after trial 50
                while len(event.getKeys(keyList=['space'])) == 0:
                    win.flip()
                Instr_2a.setAutoDraw(False)
                trials = range(50, 150)                                         # Sets up trials 51-150 experimental trials to be for-looped
            else:
                trials = range(150, 250)                                        # Sets up trials 151-250 experimental trials to be for-looped

            # Reminder for exps 2 + 4 what each cue represents, presented after trial 50 and trial 150
            bloop = 0
            while int(expInfo['session']) % 2 == 0 and bloop < 2:
                if event.getKeys(keyList=["space"]):
                    bloop += 1
                if bloop == 0:
                    Instr_2b.setAutoDraw(True)
                else:
                    Instr_2b.setAutoDraw(False)
                    Instr_2c.setAutoDraw(True)
                win.flip()
            Instr_2c.setAutoDraw(False)
        else:
            Post_Instr_1.setAutoDraw(True)
            while len(event.getKeys(keyList=["space"])) == 0:
                win.flip()
            Post_Instr_1.setAutoDraw(False)
            Post_Q1.setAutoDraw(True)

            # Asks three questions after trial 250 about whether cues could be seen
            while trialcounter < trials[-1] + 4:
                if trialcounter < trials[-1] + 3:
                    theseKeys = event.getKeys(keyList=['y', 'n'])
                else:
                    theseKeys = event.getKeys(keyList=['l', 's', 'n'])
                if theseKeys:
                    thisExp.addData('Trial', trialcounter)
                    if trialcounter < trials[-1] + 2:
                        Post_Q1.setAutoDraw(False)
                        Post_Q2.setAutoDraw(True)
                    elif trialcounter < trials[-1] + 3:
                        Post_Q2.setAutoDraw(False)
                        Post_Q3.setAutoDraw(True)
                    trialcounter += 1
                    thisExp.addData('Response', theseKeys[-1])
                    event.clearEvents(eventType='keyboard')
                    thisExp.nextEntry()
                else:
                    win.flip()
            Post_Q3.setAutoDraw(False)
            win.flip()
            trials = range(posttrials)

        # Probes about cues' meanings in exps 2 + 4, doesn't advance unless all three questions are answered correctly
        acclist = []
        random.shuffle(CueTest_list)
        cloop = 0
        Instr1.setText('In the instructions, you were informed that certain '   # Starting Instr1 that gets inherited into the start of cloop
                       'number cues either predicted task-switches (hard '
                       'trials) or task-repeats (easy trials), or were non-'
                       'predictive (neutral). Press the spacebar to continue.')
        while int(expInfo['session']) % 2 == 0 and cloop < 5:
            if cloop in [0,4]:
                if cloop == 4:
                    CueTest_list[2][0].setAutoDraw(False)
                    if rep == 1:
                        Instr1.setText('Press the spacebar to begin the '
                                       'main experiment.')
                    elif rep < 4:
                        Instr1.setText('Press the spacebar to proceed.')
                    else:
                        Instr1.setText(Post_Instr_2)
                if len(event.getKeys(keyList=['space'])) > 0:
                    cloop += 1
                Instr1.setAutoDraw(True)                                        # Instr1 gets presented twice but its text changes after the 0th iteration in cloop
            else:
                Instr1.setAutoDraw(False)
                CueTest_list[cloop - 1][0].setAutoDraw(True)
                theseKeys = event.getKeys()
                if len(theseKeys) > 0:
                    theseKeys = theseKeys[0].split('_')[-1]
                    CueTest_list[cloop - 1][0].setAutoDraw(False)
                    try:
                        theseKeys = int(theseKeys)
                        if theseKeys == CueTest_list[cloop - 1][1]:             # Checks for whether pressed key was the correct response
                            acclist.append(1)
                        else:
                            acclist.append(0)
                        event.clearEvents(eventType='keyboard')
                        if cloop == 3:                                          # When the three probes are completed...
                            if np.mean(acclist[-3:]) != 1:                      # ...and at least one was answered incorrectly:
                                random.shuffle(CueTest_list)                    # randomize the order the cues are presented for the next time
                                Instr_probe_miss.setAutoDraw(True)              # inform participant at least one response was incorrect
                                while (len(event.getKeys(keyList=["space"]))
                                        == 0):
                                    win.flip()
                                Instr_probe_miss.setAutoDraw(False)
                                cloop = 0                                       # reset cloop
                            else:                                               # When three probes are all correct, save data and proceed to next line, 'cloop += 1'
                                thisExp.addData('CueProbe', rep)
                                thisExp.addData('False_Attempts',
                                                len(acclist)/3 - 1)
                                thisExp.addData('Full_attempt_list', acclist)
                                thisExp.nextEntry()
                        cloop += 1
                    except:
                        pass
            win.flip()

        # Clear previously pressed keys and display instructions for cue-perception post-task (already took these stesps for expt 2 in the above while loop, which is why this if statement is applying specifically to expt 1)
        if expInfo['session'] == '1' and rep == 4:
            event.clearEvents(eventType='keyboard')
            Instr1.setText(Post_Instr_2)
            Instr1.setAutoDraw(True)
            while (len(event.getKeys(keyList=["space"])) == 0):
                win.flip()
        Instr1.setAutoDraw(False)



    RTF = []                                                                    # Collect RTs from trials in previous `rep`, which is used to determine the 60% RT cutoff for the upcoming 100 trials for rep == 2 and rep == 3


    ##-----------------------TRIAL FOR LOOP BEGINS----------------------------##

    for trial in trials:
        frameN = -1                                                             # Number of completed frames (so 0 is the first frame)
        t = 0
        overalltime = globalClock.getTime()
        trialClock.reset()
        continueRoutine = True                                                  # Used for knowing when to quit out of the below while loop


        ##------------------SET START & DURATION OF STIMULI-------------------##

        if rep < 4:
            ITI = trialmatrix[6][trial]
            stim_delay = trialmatrix[7][trial]
        else:
            ITI = postmatrix[1][trial]
            stim_delay = 0                                                      # There's no stimulus (or mask, for that matter) in the cue-perception task so there's no delay between mask and stimulus in that task


        ##---------------------SET TRIAL CONDITIONS---------------------------##

        # This is all just extracting from the trialmatrix
        StimLetter.setText(trialmatrix[0][trial])
        continuity = trialmatrix[1][trial]
        task = trialmatrix[2][trial]
        polygon.setLineColor(trialmatrix[3][trial])

        # Once we reach the cue-perception task we extract the cue from the postmatrix, not the main trial experimental matrix
        if rep < 4:
            Cue.setText(trialmatrix[5][trial])
            corrAns = trialmatrix[4][trial]
        else:
            Cue.setText(postmatrix[0][trial])
            corrAns = postmatrix[0][trial]

        key_resp = event.BuilderKeyResponse()
        Fixation.setAutoDraw(True)                                              # Start the fixation since it basically occurs at the exact start of the trial anyways, and if it were in the while loop it would just occur at frameN == 0
        Fixation.tStart = t


        ##--------------------------WHILE LOOP BEGINS-------------------------##

        while continueRoutine:
            if event.getKeys(keyList=["escape"]):                               # Quit experiment if the escape key is press
                core.quit()
            t = trialClock.getTime()                                            # Get the time since trial began
            frameN += 1                                                         # Advance stimulus presentation by one frame
            if rep < 4:
                theseKeys = event.getKeys(keyList=['z', 'num_3'])               # `z` and `num_3` are the only keys that will even register when they are pressed
            else:
                theseKeys = event.getKeys()                                     # For the last rep (the cue-perception task) we're interested in all key presses, not just `z` and `num_3`, so we record any key participants thought the cue was
                if len(theseKeys) > 0:                                          # Process numpad keys without their "num_" prefix...
                    theseKeys[0] = theseKeys[0].split('_')[-1]                  # ... (therefore pressing, say, 4 will be processed the same whether it was pressed on the numpad or keypad)


            ##--------------------SHAPES UPDATE-------------------------------##

            if frameN == ITI:                                                   # When the final ITI frame elapses...
                Fixation.tEnd = t                                               # record the exact time since the trial began,
                Fixation.setAutoDraw(False)                                     # remove the fixation cross from the screen,
                if rep > 0:                                                     # and during main experiment and cue perception trials,
                    Cue.tStart = t                                              # immediately record the time again
                    Cue.setAutoDraw(True)                                       # and display the cue
            elif rep > 0:
                if frameN == ITI + cue_duration:
                    Cue.tEnd = t
                    Cue.setAutoDraw(False)                                      # Remove cue
                elif (frameN == (ITI + cue_duration + mask_delay)
                                        and (int(expInfo['session']) < 3)):
                    Mask.tStart = t
                    Mask.setAutoDraw(True)                                      # Add mask for trials 1 + 2
                elif (frameN == (ITI + cue_duration + mask_delay
                        + mask_duration) and (int(expInfo['session']) < 3)):
                    Mask.tEnd = t
                    Mask.setAutoDraw(False)                                     # Subsequently remove the mask
                    if rep == 4:
                        win.callOnFlip(key_resp.clock.reset)                    # Reset clock and pressed keys before next trial in rep == 4,
                        event.clearEvents(eventType='keyboard')                 # because when these lines get called below the if statements include only rep < 4
            if ((rep == 0 and frameN == ITI) or                                 # After ITI in rep == 0 or mask-stimulus delay in exps 1-4 expire...
                (4 > rep > 0 and frameN == ITI + cue_duration
                + mask_delay + mask_duration + stim_delay)):
                polygon.tStart = t
                StimLetter.setAutoDraw(True)                                    # ...display stimulus letter,
                polygon.setAutoDraw(True)                                       # display rectangle,
                win.callOnFlip(key_resp.clock.reset)                            # reset RT clock,
                event.clearEvents(eventType='keyboard')                         # clear previously pressed keys
            elif (4 > rep > 1 and continuity == 'repeat'                        # When there's still no response and the RT threshold in reps 2 + 3 is eclipsed (doesn't apply to rep 1, though, because no RT cutoff for first 50 trials)...
                        and frameN == ITI + cue_duration + mask_delay
                             + mask_duration + stim_delay + round(rt_thresh)):
                theseKeys = [None]                                              # ...we record the response as 'none'
            if (len(theseKeys) > 0 and ((rep == 4 and frameN > ITI              # If a key was pressed during the response window or the response window has elapsed:
                        + cue_duration + mask_delay + mask_duration)
                        or (4 > rep > 0 and frameN > ITI + cue_duration
                        + mask_delay + mask_duration + stim_delay)
                        or (rep == 0 and frameN > ITI))):
                if theseKeys[-1] != None:
                    key_resp.rt = key_resp.clock.getTime()                      # Record RT for trials with a response
                if str(corrAns) in theseKeys:                                   # If the response was correct:
                    key_resp.corr = 1
                    if rep < 4:
                        corrP += 1                                              # update number of correct responses (used only for feedback after practice trials)
                        soundp = soundfiles[0]                                  # set sound to the 'ding' file
                        if rep > 0 and continuity == 'repeat':
                            RTF.append(key_resp.rt)                             # add to a list of correct RT's during repeat trials, which determines the 60% RT cutoff for the next rep
                else:                                                           # If there was no response or it was incorrect:
                    key_resp.corr = 0
                    if rep < 4:
                        soundp = soundfiles[1]                                  # set sound to the 'chord' file
                if rep < 4:
                    polygon.tEnd = t
                    StimLetter.setAutoDraw(False)
                    polygon.setAutoDraw(False)
                continueRoutine = False                                         # Trial concludes


            ##------------CHECK ALL IF COMPONENTS HAVE FINISHED---------------##

            if not continueRoutine:
                break
            else:
                win.flip()


        ##--------------------------RECORD DATA-------------------------------##

        thisExp.addData('Trial',trialcounter)
        trialcounter += 1                                                       # Update trial number
        if rep < 4:
            thisExp.addData('Task', task)
            thisExp.addData('TaskColor', polygon.lineColor)
            thisExp.addData('Continuity', continuity)
            thisExp.addData('StimLetter', StimLetter.text)
            thisExp.addData('StimLetterStartTime', polygon.tStart)
            thisExp.addData('StimLetterEndTime', polygon.tEnd)
            sound_clip.setSound(soundp, secs=-1)
            sound_clip.play()                                                   # Start the feedback sound (it finishes automatically)
        thisExp.addData('Response', theseKeys[-1])
        thisExp.addData('CorrectAnswer', corrAns)
        thisExp.addData('Accuracy', key_resp.corr)
        if theseKeys[-1] != None:
            thisExp.addData('RT', key_resp.rt)                                  # Record RT if there was a response
        thisExp.addData('fixationStartTimeinOverallExp', overalltime)
        thisExp.addData('fixationStartTime', Fixation.tStart)
        thisExp.addData('fixationEndTime', Fixation.tEnd)
        if rep != 0:                                                            # Record cue details for reps > 0
            thisExp.addData('cueStartTime', Cue.tStart)
            thisExp.addData('cueEndTime', Cue.tEnd)
            thisExp.addData('Cue', Cue.text)
            if int(expInfo['session']) < 3:                                     # Record mask details for exps 1 + 2
                thisExp.addData('maskStartTime', Mask.tStart)
                thisExp.addData('maskEndTime', Mask.tEnd)
        thisExp.nextEntry()                                                     # Advance to next line in csv in preparation for next trial



# Display end-of-study instruction screen, which advances with 'spacebar' press
event.clearEvents(eventType='keyboard')
Ending.setAutoDraw(True)
while len(event.getKeys(keyList=["space"])) == 0:
    win.flip()
Ending.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
