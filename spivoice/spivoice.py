import win32com.client as wincl
import os
list=["Rahul","Nani","Ram","akil","Ashwath","jai","Raman"]
lenlist=str(len(list))
speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
for lists in list:
    spk.Speak(f"Shout out to {lists}")