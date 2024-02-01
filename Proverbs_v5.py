import random

# Create a dictionary with the Proverbs
Words_of_the_Wise= {
    "A wise son makes a glad father, but a foolish son is the grief of his mother.": 1,
    "Treasures of wickedness profit no one, but righteousness delivers from death.": 2,
    "He becomes poor who deals with an idle hand, but the hand of the diligent makes rich.": 3,
    "He who gathers in summer is a wise son, but he who sleeps at harvest is a shameful one.": 4,
    "He who walks uprightly walks securely, but he who perverts his ways shall come to grief.": 5,
    "Hatred stirs up strife, but love covers all transgressions.": 6,
    "The rich man's wealth is his strong city, the destruction of the poor is their poverty.": 7,
    "He who hides hatred has lying lips, and he who utters slander is a fool.": 8,
    "In a multitude of words there is room for transgressions, but he who controls his lips acts wisely.": 9,
    "The lips of the righteous feed many, but the foolish die for lack of un-derstanding.":10,
    "It is like sport to the fool to do wrong,as is wisdom to a man of understanding.":11,
    "As vinegar is to the teeth,and smoke to the eyes,is the sluggard to those who send him.": 12,
    "A false scale is an abomination to the Lord, but a just weight is his de-light.": 13,
    "When pride comes, then comes shame; but with the lowly is wisdom.": 14,
    "Riches are of no avail in the day of wrath, but righteousness saves from death.": 15,
    "When a wicked man dies, his hope perishes; and the expectation of his children perishes with him": 16,
    "A talebeaer reveals secrets, but the faithful conceal the matter": 17,
    "For want of a guidance a people will fall, but in many counselors there is saftey.": 18,
    "A gracious woman obtains honor, and a strong man obtains riches.": 19,
    "Like an ornament of gold in a swine's snout, so is beauty in a woman without taste.": 20,
    "The generous soul shall be enriched, and he who satisfies shall himself be satisfied.": 21,
    "He who withholds grain, the people shall curse; but blessings shall fall upon the head of him who sells it": 22,
    "He who trusts in his riches wil fall, but the righteous will flourish like a green leaf.": 23,
    "He who troubles his own house shall inherit the wind, and the foolish shall be servant to the wise of heart.": 24,
    "He who loves knowledge loves correction, but he who hates reproof is brutish.": 25,
    "A good woman is a crown to her husband; she who brings him shame is like rot in his bones.": 26,
    "A righteous man has regard for the life of his beast, but even the tender mercies of the wicked are cruel.": 27,
    "The way of a fool seems right in his own eyes;he who is wise listens to counsel": 28,
    "A fool's vexation is soon known, but a prudent man conceals shame" :29,
    "Deceit is in the heart of those who devise evil,but the conselors of peace have joy.":30,
    "Lying lips are an abomination to the Lord; those who deal truthfully are his delight.": 31,
    "A prudent man conceals his knowledge, but the fool proclaims his foolishness.": 32,
    "Care in the heart of a man bows him down, but a good word makes him glad": 33,
    "From the fruit of his mouth the good man eats, and the faithless, violence":34,
    "the sluggard desires and gains nothing, while the diligent is amply rewarded":35,
    "Wealth gained by vanity shall be diminished, but he who gathers by labor shall increase": 36,
    "Hope deferred makes the heart sick,but desire fulflled is a tree of life": 37,
    "The teaching of the wise is a fountain of life, that one may avoid the snares of death.": 38,
    "A wicked messenger falls into evil, but a faithful messenger brings healing.":39,
    "Poverty and shame come to him who refuses correction, but he who accepts reproof shall be honored.":40,
    "He who walks with wise men shall be wise, but the companion of fools shall suffer harm.":41,
    "A good man leaves an inheritance to his children's children, but the wealth of the sinner is laid up for the righteous": 42,
    "Much food is in the tillage of the poor, but much is swept away by in justice.":43,
    "He who spares the rod hates his son; he who loves his son chastens him betimes.":44,
    "The wise woman builds her house, but the foolish one tears it down with her own hands.": 45,
    "When there are no oxen, the crib is empty; but by the strength of the ox comes abundance.":46,
    "A scoffer seeks wisdom and finds it not, but knowledge is easy for him who has discernment.":47,
    "The heart knows its own bitterness, and a stranger cannot share in its joy.":48,
    "There is a way which seems right to a man, but in the end it leads to death.":49,
    "The thoughtless believe every word, but the prudent man watches his every step.":50,
    "He who is soon angry deals foolishly,and a man of wicked devices is hated.":51,
    "The poor is hated even by his neighbor, but the rich have many friends.":52,
    "He who despises his neighbor sins, but happy is he who is gracious to the humble.":53,
    "In all labor there is profit, but mere talk tends only to penury.":54,
    "He who is slow to anger has great understanding, but he who becomes easily angered exalts folly.":55,
    "A tranquil heart prolongs life, but envy is a rot in the bones.":56,
    "He who oppresses the poor blasphemes his Maker, but he who has mercy on the needy honors him": 57,
    "A soft answer turns away wrath, but harsh words stir up anger.": 58,
    "A soothing tongue is a tree of life, but perverseness in it wounds the spirit.":59,
    "In the house of the righteous there is much treasure, but in the revenues of the wicked, only trouble.":60,
    "A merry heart makes a cheerful countenance, but by sorrow of heart the spirit is broken.":61,
    "All the days of the poor are sorrowful, but he of a merry heart has a continual feast.":62,
    "Better is little, with fear of the Lord, than great treasure, and with it trouble":63,
    'Better a dinner of Herbs where love is, than a roasted ox with hatred':64,
    'A wise son honors his Father, but a foolish one despises his Mother':65,
    'To the wise the path of life goes upward, away from Sheol below.':66,
    'The Lord is far from the wicked, but he is near to the righteous.':67,
    'The wrath of a king is like a messenger of death, and a wise man will pacify it.':68,
    'How much better it is to get wisdom than gold, to get understanding rather than silver.':69,
    'Pride goes before destruction, and a haughty spirit before a fall.':70,
    'A well spring of life it is to teach the wise, but to teach the fool is folly.':71,
    'Pleasant words are like honey, sweet to the soul and health to the body.':72,
    'A perverse man sows strife,and a whisperer separates friends':73,
    'He who is slow to anger is better than the mighty, and he who rules his temper than he who conquers a city.':74,
    'The lot is cast, but disposing of it is from the Lord.':75.,
    'Better a dry morsel in peace than a house full of feasting with strife':76,
    'The refining pot is for silver and the furnace for gold,but the Lord tries the heart.':77,
    'An evildoer heeds wicked lips,and a liar heeds the mischievous tongue.':78,
    'He who mocks the poor blasphemes his Maker, and he who i s glad-dened by calamity will not go unpunished.':79,
    'A rebuke cuts deeper into one who has understanding than a hundred stripesintoa tool.':80,
    'Let a man meet a bear robbed of her whelps rather than a fool bent on his folly.':81,
    'He who rewards evil for good, evil shall not depart from his house.':82,
    'He who justifies the wicked, and he who condemns the righteous, both are an abomination to the Lord':83,
    'Why is there a price in the hand of a fool to buy wisdom, seeing that he has no understanding?':84,
    'He who begets a fool does it to his sorrow, and the father of a fool has no joy.':85,
    'A merry heart is good medicine, but a broken spirit dries up the bones.':86,
    'Even a fool,when he holds his peace,is accounted wise;when he shuts his lips, he is esteemed as prudent.':87,
    'With wickedness comes contempt, and with dishonor comes disgrace.':88,
    'he words of a mans mouth are as deep waters; the wellspring of wisdom is as a flowing brook.':89,
    'A fools mouth is his ruin, and his lips are the snare of his soul.':90,
    'The words of a gossip are wounds that go down into the inner most parts of the belly.':91,




#top of 498


    
}

# Get a random key from the dictionary
random_key = random.choice(list(Words_of_the_Wise.keys()))

# Access the corresponding value
random_value = Words_of_the_Wise[random_key]

print("Proverb: ", random_key)
print(random_value)

