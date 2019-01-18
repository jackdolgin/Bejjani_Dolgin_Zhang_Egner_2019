# Disentangling the roles of cue visibility and knowledge in learning cognitive control
A task-switching paradigm classifying a word as either capitalized/lowercase or a consononant/vowel. Before the word appears on each trial, a cue appears for 11 ms, presented either subliminally (with a mask) or supraliminally (without a mask) depending on the experiment. Two of these cues precede a single task, and the third precedes both tasks.

## Publication

Preregistered Direct Replication, Stage 1 in principle acceptance at *Psychological Science*; registration available [here](https://osf.io/7jfbp/).

## Organization
* Stimuli used in the experiment, namely two .png images and two .wav clips, are stored in (stimuli)[stimuli].
* The task script for all four experiments in this study are in a single python file, (Script_all_Exps.py)[Script_all_Exps.py]. Entering the session number in the script's popup corresponds with the experiment number. The post-task for experiments 1 and 2 can also be run from this script. 
* The post-task test for experiments 3 and 4 and the demographics form for all four studies can be found in the (Post_Task)[Post_Task] directory. 

## Dependencies
The task script was written in PsychoPy [1.90.3](https://github.com/psychopy/psychopy/releases/tag/1.90.3) utilizing Python [3.7.0](https://www.python.org/downloads/release/python-370/)
