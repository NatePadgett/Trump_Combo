# Trump_Combo

Last you heard from me I was working with a transcript from President Donald Trump's first press conference after his election. For that project, I pulled out lines of text that contained the word "fake" and remixed them into a random narrative about what the president considers fake news. Explore Fake_Trumps [here](https://github.com/NatePadgett/Fake_TRUMPS).

For this projects I decided to continue working with the same source material, but combine it with the transcript from a recent interview Trump had with Time magazine about truth and the state of his presidency. You can find the source text [here](http://time.com/4710456/donald-trump-time-interview-truth-falsehood/).

GOAL
To shorten and combine both Transcripts in such a way that the texts seemed to be from the same interview and to blur the lines between what was asked of the president and what he himself said. This wasn't motivated by politics; I am simply exploring combining text and readability thereafter. 

CODE OVERVIEW
I wrote two scripts, one to parse out the words in both transcripts and sort them by most frequently occurring, and another to remix lines from both that contain the transcripts' respective most commonly occurring words. File word_count.py obviously counts the words, while Trump_Combine.py combines the lines from both files. 

With word_count.py, I organized the words of each file into a dictionary called wordcount, with the keys being the words and the values being the number of occurances of a given word. You can see the for loop "for word in words" which contains an if statement for counting the number of instances of a word after it is intially added to the dictionary. I initially struggled to figure out how to sort the list of words by their frequency (values), but the line comprehension you see for the variable wordtuple works. It's not very pythonic, but gets the job done for my purposes here. Something to keep working on if I stick with this project. I used this script to produce two word count text files which were then processed alongside the source texts with Trumps_Combine.py.

Trumps_Combine.py takes the raw text of each transcript, searches for the the top 10-20 words in each transcript (stored in separate files and combined in this script), stores the lines containing those words, and prints a random sampling of those lines. 

RESULTS
The products of this projects were interesting and (I think) fulfilled the goal I set out to achieve. Here are three of my favorites:

Trump_Combo 1
-------------

TRUMP: No, no, one question. Two we can't handle. This room can't handle two. Go ahead, give me the better of your two.
And it was totally -- they totally misrepresented those very wonderful women, I have to tell you, totally misrepresented. I said give us the retraction. They never gave us a retraction and frankly, I then went on to other things.
In the meantime, Mosul is very, very difficult. Do you know why? Because I don't talk about military, and I don't talk about certain other things, you're going to be surprised to hear that. And by the way, my whole campaign, I'd say that. So I don't have to tell you. I don't want to be one of these guys that say, "Yes, here's what we're going to do." I don't have to do that. I don't have to tell you what I'm going to do in North Korea.
TRUMP: And I'm reading the order, I'm saying, why aren't we using American steel? And they said, that's a good idea, we put it in. To drain the swamp of corruption in Washington, D.C., I've started by imposing a five-year lobbying ban on White House officials and a lifetime ban on lobbying for a foreign government.
This last month has represented an unprecedented degree of action on behalf of the great citizens of our country. Again, I say it. There has never been a presidency that's done so much in such a short period of time. And we have not even started the big work yet. That starts early next week.
QUESTION: (OFF-MIKE) said today that you have big intellectual margins (inaudible) 300 or more (ph), or 350 (ph) electoral (ph) votes. President Obama about 365 (OFF-MIKE).
Now, they'll take this news conference -- I'm actually having a very good time, OK? But they'll take this news conference -- don't forget, that's the way I won. Remember, I used to give you a news conference every time I made a speech, which was like every day. OK?
And that's a shame because if we could get along with Russia - and by the way, China and Japan and everyone. If we could get along, it would be a positive thing, not a negative thing.
Well, that's what I've been talking about for a year and a half, strong borders. They're so surprised, oh, he having strong borders, well that's what I've been talking about to the press and to everybody else. One promise after another after years of politicians lying to you to get elected. They lied to the American people in order to get elected. Some of the things I'm doing probably aren't popular but they're necessary for security and for other reasons.
I mean that. I would be your biggest fan in the world if you treated me right. I sort of understand there's a certain bias maybe by Jeff (ph) or somebody, you know - you know, whatever reason. But - and I understand that. But you've got to be at least a little bit fair and that's why the public sees it. They see it. They see it's not fair. You take a look at some of your shows and you see the bias and the hatred.

Trump_Combo 2
-------------

The gentleman you mentioned is a very talented man, very successful man and he's offered his services and you know, it's something we may take advantage of. But I don't think we're need that at all because of the fact that you know, I think that we are gonna be able to straighten it out very easily on its own.
He then, called me up extremely nicely to congratulate me on the inauguration, which was terrific. But so did many other leaders, almost all other leaders from almost all of the country. So that's the extent.
Why did Hillary Clinton announce that, "I'm sorry, but I have been given the questions to a debate or a town hall, and I feel that it's inappropriate, and I want to turn in CNN for not doing a good job." QUESTION: And if I may follow up on that, just something that Jonathan Karl (ph) was asking you about. You said that the leaks are real, but the news is fake. I guess I don't understand. It seems that there's a disconnect there. If the information coming from those leaks is real, then how can the stories be fake?
QUESTION: And she does a lot of great work for the country as well (ph). Can you talk a little bit about what's first for (ph) Melania Trump does for the country and (inaudible) so opening White House Visitors Office, what does that mean...
QUESTION: There was a ballistic missile test that many interpret as a violation of an agreement between the two countries; and a Russian plane buzzed a U.S. destroyer.
The information was provided by -- who I don't know, Sally Yates. And I was a little surprised because I said "doesn't sound like he did anything wrong there." But he did something wrong with respect to the vice president and I thought that was not acceptable. As far as -- as far as the actual making the call, fact I've watched various programs and I've read various articles where he was just doing his job.
I think I'll say a few words, and then we'll take some questions. And I had this time. We've been negotiating a lot of different transactions to save money on contracts that were terrible, including airplane contracts that were out of control and late and terrible; just absolutely catastrophic in terms of what was happening. And we've done some really good work. We're very proud of that.
But the DACA situation is a very, very -- it's a very difficult thing for me because you know, I love these kids, I love kids, I have kids and grandkids. And I find it very, very hard doing what the law says exactly to do and you know, the law is rough.
TRUMP: All of those things that you mentioned are very recent, because probably Putin assumes that he's not going to be able to make a deal with me because it's politically not popular for me to make a deal. So Hillary Clinton tries a re-set. It failed. They all tried. But I'm different than those people.
And one more thing, I have kept my promise to the American people by nominating a justice of the United States Supreme Court, Judge Neil Gorsuch, who is from my list of 20, and who will be a true defender of our laws and our Constitution, highly respected, should get the votes from the Democrats. You may not see that. But he'll get there one way or the other. But he should get there the old-fashioned way, and he should get those votes.

Trump_Combo 3
-------------

QUESTION: What are you going to do about - what are you going to do about (inaudible).
And just while you're at it, because you mentioned this, Wall Street Journal did a story today that was almost as disgraceful as the failing New York Time's story, yesterday. And it talked about -- these are (ph) front page.
Hillary Clinton - that was the reset, remember it said reset? Now if I do that, oh, I'm a bad guy. If we could get along with Russia, that's a positive thing. We have a very talented man, Rex Tillerson, who's going to be meeting with them shortly and I told him. I said "I know politically it's probably not good for me." The greatest thing I could do is shoot that ship that's 30 miles off shore right out of the water.
TRUMP: Well, I had nothing to do with it. I have nothing to do with Russia. I told you, I have no deals there, I have no anything. Now, when WikiLeaks, which I had nothing to do with, comes out and happens to give, they're not giving classified information. They're giving stuff -- what was said at an office about Hillary cheating on the debates.
I will not back down from defending our country. I got elected on defense of our country. I keep my campaign promises, and our citizens will be very happy when they see the result. They already are, I can tell you that. Extreme vetting will be put in place and it already is in place in many places.
TRUMP: Tax reform is going to happen fairly quickly. We're doing Obamacare. We're in final stages. We should be submitting the initial plan in March, early March, I would say. And we have to, as you know, statutorily and for reasons of budget, we have to go first. It's not like, frankly, the tax would be easier, in my opinion, but for statutory reasons and for budgetary reasons, we have to submit the healthcare sooner.
TRUMP: Well, that's -- well, you know, we do have other people. You do have other people and your ratings aren't as good as some of the other people that are waiting.
Let me tell you about the travel ban. We had a very smooth rollout of the travel ban. But we had a bad court. Got a bad decision. We had a court that's been overturned. Again, may be wrong. But I think it's 80 percent of the time, a lot.
Now, I don't know that we're going to make a deal. I don't know. We might. We might not. But it would be much easier for me to be so tough -- the tougher I am on Russia, the better. But you know what? I want to do the right thing for the American people. And to be honest, secondarily, I want to do the right thing for the world.
I have great people lined up to help with the inner cities. OK?


