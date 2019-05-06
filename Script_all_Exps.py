from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
import numpy as np                                                              # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os                                                                       # handy system and path functions
import sys                                                                      # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = (os.path.dirname(
            os.path.abspath(__file__)).decode(sys.getfilesystemencoding()))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'PDR_script'                                                          # from the Builder filename that created this script
expInfo = {'participant':'','session':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()                                                                 # user pressed cancel during popout
expInfo['date'] = data.getDateStr()                                             # add a simple timestamp
expInfo['expName'] = expName

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, allowGUI=False,
    monitor='testMonitor', color=[1,1,1], useFBO=True)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()

#Create randomized list of cue conditions for different participants, counterbalanced; this randomly-generated list is used for all participants, hence the next two lines are commented out
# cueversions = np.repeat([0,1,2,3,4,5],4)
# np.random.shuffle(cueversions)

if int(expInfo['session']) == 1:
    cueversions = [3,0,3,3,2,3,1,4,2,5,0,5,4,2,5,1,0,4,2,5,4,1,0,1,5.0,1,3,2,4,
                  2,5,4,2,5,3]
elif int(expInfo['session']) == 2:
    cueversions = [1,2,5,4,1,5,4,0,0,1,4,4,0,2,3,2,3,3,5,1,0,5,3,2,1,3,5,4,0,2,
                   0,2,4,1,3,5,3,4,0,1,2,1,4,0,3,4,2,1,5,1,3,5]
elif int(expInfo['session']) == 3:
    cueversions = [4,4,4,4,2,5,0,1,5,5,1,4,3,0,2,4,1,3,3,1,3,2,0,0,5,2,3,4]
elif int(expInfo['session']) == 4:
    cueversions = [1,2,2,2,3,3,4,5,1,5,0,0,2,0,0,4,1,3,3,5,4,5,4,1,0,2,4,1,3,5,4,2,3,1,0,5]

CueVersion = cueversions[int(expInfo['participant'])%100 - 1]

expInfo['cueVersion'] = CueVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = (_thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'],
           expName, "ses_" + expInfo['session']))

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)                                       # this outputs to the screen, not a file




##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##
##-----------------------------START CODE-------------------------------------##
##----------------------------------------------------------------------------##
##----------------------------------------------------------------------------##



##----------------------------------------------------------------------------##
##--------------------------SET UP STIMULI------------------------------------##
##----------------------------------------------------------------------------##


##--------------------------SET UP TEXT & CUES--------------------------------##

lowvowelSet = ['a','e','i','o','u']
capvowelSet = ['A','E','I','O','U']
lowconsonantSet = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s',
                   't','v','w','x','y','z']
capconsonantSet = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S',
                   'T','V','W','X','Y','Z']
instr_letters = ['O','o','K','k','U','u','S','s','C','c','W','w','Z','z','V',
                 'v','X','x']

cuelist = [[2,4,8,],[2,8,4],[4,2,8],[4,8,2],[8,2,4],[8,4,2]]
cueSet = cuelist[CueVersion]
cueA = cueSet[0]                                                                # cue for predictive switch
cueB = cueSet[1]                                                                # non-predictive cue
cueC = cueSet[2]                                                                # cue for predictive repeat


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

if int(expInfo['session']) < 3:

    Instr_1c = visual.TextStim(win=win, name='Instr_1c', color='black',
        text = ('On each trial, a pattern of five Xs will appear on-screen '
              'followed by a letter that you will categorize according to the '
              'color of its surrounding rectangle. The Xs are not relevant to '
              'the task that you are performing.'))

    Instr_1c_2 = visual.TextStim(win=win, name='Instr_1c_2', color='black',
        text = ('However, before the Xs are presented, number cues will flash '
               'on-screen. One of these cues ("' + cueAinstr))

    Instr_1c_3 = visual.TextStim(win=win, name='Instr_1c_3', color='black',
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

    Instr_1c_2 = visual.TextStim(win=win, name='Instr_1c_2', color='black',
        text = ('One of these cues ("' + cueAinstr + ' One of the cues ("'
                + cueCinstr))

    Instr_1c_3 = visual.TextStim(win=win, name='Instr_1c_3', color='black',
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

Mapping = visual.ImageStim(win=win, name='Mapping',
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

CueTest_list = [[CueTestA, cueA], [CueTestB, cueB], [CueTestC, cueC]]

Instr_probe_miss = visual.TextStim(win=win, name='Instr_probe_miss',
    color='black', text = ('You answered at least one of the three '
                            'cue-related questions incorrectly. Please '
                            'press the spacebar to try again.'))

Post_Instr_1 = visual.TextStim(win=win, name='Post_Instr_1', color='black',
    text = ('Welcome to the post-test! You will answer a few questions about '
           'the experimental stimuli and do some judgement tasks. Press the '
           'spacebar to continue.'))

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


##---------------------------SOUND NOISE & LOUDNESS---------------------------##

sound_clip = sound.Sound('A', secs=-1)
sound_clip.setVolume(1)
soundfiles = [os.path.join('stimuli','ding.wav'),
              os.path.join('stimuli','chord.wav')]


##-------------------------INTERVALS & DURATION SIZES-------------------------##

framelength = win.monitorFramePeriod

fix_duration_min = 170                                                          # 2000 ms in Farooqui
fix_duration_max = 255                                                          # 3000 ms in Farooqui
cue_duration = 1                                                                # 11.7 ms in Farooqui
mask_delay = 2                                                                  # 23.2 ms in Farooqui
if int(expInfo['session']) < 3:
    mask_duration = 42                                                          # 500 ms in Farooqui
else:
    mask_duration = 0
stim_delay_min = 127                                                            # 1500 ms in Farooqui
stim_delay_max = 212                                                            # 2500 ms in Farooqui


##--------------------------------CREATE TIMERS-------------------------------##

globalClock = core.MonotonicClock()                                             # to track the time since experiment started
trialClock = core.Clock()                                                       # unlike globalclock, gets reset each trial


##---------------------------TRIAL MATRIX & RANDOMIZATION---------------------##

SRmapping_full = ['z', 'num_3']
taskColorRGB = ["#0000ff","#00ff00"]                                            # blue, green

ptrials = 12
maintrials = 250
posttrials = 30
extra_appearances = ([1,1,0,0])

def expmatrix(trials):
    Cue = ([cueA]*int(round(trials*.25*.5)) + [cueB]*int(round(trials*.5))
           + [cueC]*int(round(trials*.75*.5)))

    if trials == ptrials:
        continuity = (['repeat']*int((trials/2)) + ['switch']
                     + ['repeat']*int((trials/2) - 1))
        currentTask = 1
    else:
        continuity = ['switch']*62 + ['repeat']*188
        currentTask = random.choice([1,2])
        toshuffle = list(zip(continuity, Cue))
        random.shuffle(toshuffle)
        continuity[:], Cue[:] = zip (*toshuffle)

    np.random.shuffle(lowvowelSet)
    np.random.shuffle(capvowelSet)
    np.random.shuffle(lowconsonantSet)
    np.random.shuffle(capconsonantSet)
    np.random.shuffle(extra_appearances)

    #which stims appears
    if trials == ptrials:
        stimSet = (lowconsonantSet[:3] + capconsonantSet[:3]
                  + lowvowelSet[:3] + capvowelSet[:3])
    else:
        stimSet = (lowconsonantSet*2 + capconsonantSet*2 + lowvowelSet*12
                   + capvowelSet*12 + lowconsonantSet[0+extra_appearances[0]:]
                   + capconsonantSet[0+extra_appearances[1]:]
                   + lowvowelSet[2 + extra_appearances[2]:]
                   + capvowelSet[2 + extra_appearances[3]:])

    np.random.shuffle(stimSet)

    task = []
    corrAns = []
    taskColor = []
    fix_duration = []
    stim_delay = []

    for tr in range(len(continuity)):
        if continuity[tr] == 'repeat':
            task.append(currentTask)
        else:
            task.append(3-currentTask)
        currentTask = task[tr]
        if ((currentTask == 1 and stimSet[tr] in (lowvowelSet + capvowelSet))
           or (currentTask == 2 and stimSet[tr].islower())):
            corrAns.append(SRmapping_full[0])
        else:
            corrAns.append(SRmapping_full[1])
        if currentTask == 1:
            taskColor.append(taskColorRGB[0])
            task[tr] = 'vowel/consonant'
        else:
            taskColor.append(taskColorRGB[1])
            task[tr] = 'upper/lowercase'
        fix_duration.append(random.randint(fix_duration_min, fix_duration_max))
        stim_delay.append(random.randint(stim_delay_min, stim_delay_max))

    return [stimSet, continuity, task, taskColor, corrAns, Cue,
            fix_duration, stim_delay]

maintrialmatrix = expmatrix(maintrials)
postCues = np.repeat(cueSet, posttrials/len(cueSet))
np.random.shuffle(postCues)
postmatrix = [postCues, [random.randint(fix_duration_min, fix_duration_max) for i in range(posttrials)]]



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
    if instr not in range(3,5) or int(expInfo['session']) % 2 == 0:
        instr_list[instr].setAutoDraw(True)
        while len(event.getKeys(keyList=["space"])) == 0:
            win.flip()
        instr_list[instr].setAutoDraw(False)


##-------------------------START PSEUDO-PRACTICE------------------------------##

for trial in range(len(instr_letters)):
    StimLetter.setText(instr_letters[trial])
    if trial%2 == 0:
        taskColorinstr = taskColorRGB[random.choice([0,1])]
        textinstr = "This is an uppercase."
    else:
        textinstr = "This is a lowercase."
    polygon.setLineColor(taskColorinstr)
    InstrText.setText(textinstr)
    [a_stim.setAutoDraw(True) for a_stim in [InstrText, polygon, StimLetter]]
    while len(event.getKeys(keyList=['space'])) == 0:
        win.flip()

[a_stim.setAutoDraw(False) for a_stim in [InstrText, polygon, StimLetter]]
Instr_1j.setAutoDraw(True)
while len(event.getKeys(keyList=['space'])) == 0:
    win.flip()
Instr_1j.setAutoDraw(False)



##----------------------------------------------------------------------------##
##-----------------------------START TRIALS-----------------------------------##
##----------------------------------------------------------------------------##


corrP = 0
trialcounter = -ptrials
trialmatrix = expmatrix(ptrials)
trials = range(ptrials)
for rep in range(5 - (int(expInfo['session']))/3):


    ##--------------------------START MAIN EXPERIMENT-------------------------##

    if rep > 0:
        trialmatrix = maintrialmatrix
        if rep == 1:
            if int(expInfo['session']) % 2 == 0:
                Instr1.setText('Your accuracy on the practice task was '
                               + str(corrP) + ' out of 12. If you are confused '
                               'about the response keys for each task, please '
                               'call over the experimenter. Press the spacebar '
                               'to continue.')
            else:
                Instr1.setText('Your accuracy on the practice task was '
                               + str(corrP) + ' out of 12. If you are confused '
                               'about the response keys for each task, please '
                               'call over the experimenter. Press the spacebar '
                               'to begin the main experiment.')
            Instr1.setAutoDraw(True)
            while len(event.getKeys(keyList=['space'])) == 0:
                win.flip()
            Instr1.setAutoDraw(False)
            trials = range(50)
        elif rep < 4:
            rt_thresh = float(np.percentile(RTF, 60, interpolation = 'nearest'))/framelength
            if rep == 2:
                Instr_2a.setAutoDraw(True)
                while len(event.getKeys(keyList=['space'])) == 0:
                    win.flip()
                Instr_2a.setAutoDraw(False)
                trials = range(50, 150)
            else:
                trials = range(150, 250)
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
        acclist = []
        random.shuffle(CueTest_list)
        cloop = 0
        Instr1.setText('In the instructions, you were informed that certain '
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
                        Instr1.setText('In this session, a letter, digit, or '
                                       'symbol will be presented before the 5 '
                                       'Xs. If you can see or guess its '
                                       'identity, press the corresponding key '
                                       '(e.g., if you see 7, press 7; if you '
                                       'see \'b\', press b). If you did not '
                                       'see anything and cannot guess, then '
                                       'press enter. There is no time limit to '
                                       'respond if you are uncertain about '
                                       'your response. Press the spacebar '
                                       'to begin.')
                if len(event.getKeys(keyList=['space'])) > 0:
                    cloop += 1
                Instr1.setAutoDraw(True)
            else:
                Instr1.setAutoDraw(False)
                CueTest_list[cloop - 1][0].setAutoDraw(True)
                theseKeys = event.getKeys()
                if len(theseKeys) > 0:
                    theseKeys = theseKeys[0].split('_')[-1]
                    CueTest_list[cloop - 1][0].setAutoDraw(False)
                    try:
                        theseKeys = int(theseKeys)
                        if theseKeys == CueTest_list[cloop - 1][1]:
                            acclist.append(1)
                        else:
                            acclist.append(0)
                        event.clearEvents(eventType='keyboard')
                        if cloop == 3:
                            if np.mean(acclist[-3:]) != 1:
                                random.shuffle(CueTest_list)
                                Instr_probe_miss.setAutoDraw(True)
                                while (len(event.getKeys(keyList=["space"]))
                                        == 0):
                                    win.flip()
                                Instr_probe_miss.setAutoDraw(False)
                                cloop = 0
                            else:
                                thisExp.addData('CueProbe', rep)
                                thisExp.addData('False_Attempts',
                                                len(acclist)/3 - 1)
                                thisExp.addData('Full_attempt_list', acclist)
                                thisExp.nextEntry()
                        cloop += 1
                    except:
                        pass
            win.flip()
        Instr1.setAutoDraw(False)



    RTF = []                                                                    #collect RTs from previous trials


    ##-----------------------TRIAL FOR LOOP BEGINS----------------------------##

    for trial in trials:
        frameN = -1                                                             # number of completed frames (so 0 is the first frame)
        t = 0
        overalltime = globalClock.getTime()
        trialClock.reset()                                                      # clock
        continueRoutine = True


        ##------------------SET START & DURATION OF STIMULI-------------------##

        #fix_duration jittering 2000-3000 ms
        fix_duration = random.randint(fix_duration_min, fix_duration_max)
        #Time between mask and stim jittering 1500-2500 ms
        if rep < 4:
            fix_duration = trialmatrix[6][trial]
            stim_delay = trialmatrix[7][trial]
        else:
            fix_duration = postmatrix[1][trial]
            stim_delay = 0


        ##---------------------SET TRIAL CONDITIONS---------------------------##

        StimLetter.setText(trialmatrix[0][trial])
        continuity = trialmatrix[1][trial]
        task = trialmatrix[2][trial]
        polygon.setLineColor(trialmatrix[3][trial])
        if rep < 4:
            Cue.setText(trialmatrix[5][trial])
            corrAns = trialmatrix[4][trial]
        else:
            Cue.setText(postmatrix[0][trial])
            corrAns = postmatrix[0][trial]

        key_resp = event.BuilderKeyResponse()
        Fixation.setAutoDraw(True)
        Fixation.tStart = t


        ##--------------------------WHILE LOOP BEGINS-------------------------##

        while continueRoutine:
            if event.getKeys(keyList=["escape"]):
                core.quit()
            # get current time
            t = trialClock.getTime()
            frameN += 1
            if rep < 4:
                theseKeys = event.getKeys(keyList=['z', 'num_3'])
            else:
                theseKeys = event.getKeys()
                if len(theseKeys) > 0:
                    theseKeys[0] = theseKeys[0].split('_')[-1]


            ##--------------------SHAPES UPDATE-------------------------------##

            if frameN == fix_duration:
                Fixation.tEnd = t
                Fixation.setAutoDraw(False)
                if rep > 0:
                    Cue.tStart = t
                    Cue.setAutoDraw(True)
            elif rep > 0:
                if frameN == fix_duration + cue_duration:
                    Cue.tEnd = t
                    Cue.setAutoDraw(False)
                elif (frameN == (fix_duration + cue_duration + mask_delay)
                                        and (int(expInfo['session']) < 3)):
                    Mask.tStart = t
                    Mask.setAutoDraw(True)
                elif (frameN == (fix_duration + cue_duration + mask_delay
                        + mask_duration) and (int(expInfo['session']) < 3)):
                    Mask.tEnd = t
                    Mask.setAutoDraw(False)
                    if rep == 4:
                        win.callOnFlip(key_resp.clock.reset)                    # t=0 on next screen flip
                        event.clearEvents(eventType='keyboard')
            if ((rep == 0 and frameN == fix_duration) or
                (4 > rep > 0 and frameN == fix_duration + cue_duration
                + mask_delay + mask_duration + stim_delay)):
                polygon.tStart = t
                StimLetter.setAutoDraw(True)
                polygon.setAutoDraw(True)
                win.callOnFlip(key_resp.clock.reset)
                event.clearEvents(eventType='keyboard')
            elif (4 > rep > 1 and continuity == 'repeat'
                        and frameN == fix_duration + cue_duration + mask_delay
                             + mask_duration + stim_delay + round(rt_thresh)):
                theseKeys = [None]
            if (len(theseKeys) > 0 and ((rep == 4 and frameN > fix_duration
                        + cue_duration + mask_delay + mask_duration)
                        or (4 > rep > 0 and frameN > fix_duration + cue_duration
                        + mask_delay + mask_duration + stim_delay)
                        or (rep == 0 and frameN > fix_duration))):              # at least one key was pressed
                if theseKeys[-1] != None:
                    key_resp.rt = key_resp.clock.getTime()
                # was this 'correct'?
                if str(corrAns) in theseKeys:
                    key_resp.corr = 1
                    if rep < 4:
                        corrP += 1
                        soundp = soundfiles[0]
                        if rep > 0 and continuity == 'repeat':
                            RTF.append(key_resp.rt)
                else:
                    key_resp.corr = 0
                    if rep < 4:
                        soundp = soundfiles[1]
                if rep < 4:
                    polygon.tEnd = t
                    StimLetter.setAutoDraw(False)
                    polygon.setAutoDraw(False)
                # a response ends the routine
                continueRoutine = False


            ##------------CHECK ALL IF COMPONENTS HAVE FINISHED---------------##

            if not continueRoutine:
                break
            else:
                win.flip()


        ##--------------------------RECORD DATA-------------------------------##

        thisExp.addData('Trial',trialcounter)
        trialcounter += 1
        if rep < 4:
            thisExp.addData('Task', task)
            thisExp.addData('TaskColor', polygon.lineColor)
            thisExp.addData('Continuity', continuity)
            thisExp.addData('StimLetter', StimLetter.text)
            thisExp.addData('StimLetterStartTime', polygon.tStart)
            thisExp.addData('StimLetterEndTime', polygon.tEnd)
            sound_clip.setSound(soundp, secs=-1)
            sound_clip.play()                                                   # start the sound (it finishes automatically)
        thisExp.addData('Response', theseKeys[-1])
        thisExp.addData('CorrectAnswer', corrAns)
        thisExp.addData('Accuracy', key_resp.corr)
        if theseKeys[-1] != None:                                               # we had a response
            thisExp.addData('RT', key_resp.rt)
        thisExp.addData('fixationStartTimeinOverallExp', overalltime)
        thisExp.addData('fixationStartTime', Fixation.tStart)
        thisExp.addData('fixationEndTime', Fixation.tEnd)
        if rep != 0:
            thisExp.addData('cueStartTime', Cue.tStart)
            thisExp.addData('cueEndTime', Cue.tEnd)
            thisExp.addData('Cue', Cue.text)
            if int(expInfo['session']) < 3:
                thisExp.addData('maskStartTime', Mask.tStart)
                thisExp.addData('maskEndTime', Mask.tEnd)
        thisExp.nextEntry()




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
