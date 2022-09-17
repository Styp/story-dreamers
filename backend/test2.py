
from transformers import BartForConditionalGeneration, BartTokenizer


text = """
ONCE there was a gentleman who married, for his second wife, the proudest and most haughty woman that was ever seen. She had, by a former husband, two daughters of her own humor, who were, indeed, exactly like her in all things. He had likewise, by another wife, a young daughter, but of unparalleled goodness and sweetness of temper, which she took from her mother, who was the best creature in the world.

No sooner were the ceremonies of the wedding over but the mother-in-law began to show herself in her true colors. She could not bear the good qualities of this pretty girl, and the less because they made her own daughters appear the more odious. She employed her in the meanest work of the house: she scoured the dishes, tables, etc., and scrubbed madam's chamber, and those of misses, her daughters; she lay up in a sorry garret, upon a wretched straw bed, while her sisters lay in fine rooms, with floors all inlaid, upon beds of the very newest fashion, and where they had looking-glasses so large that they might see themselves at their full length from head to foot.

The poor girl bore all patiently, and dared not tell her father, who would have rattled her off; for his wife governed him entirely. When she had done her work, she used to go into the chimney-corner, and sit down among cinders and ashes, which made her commonly be called Cinderwench; but the youngest, who was not so rude and uncivil as the eldest, called her Cinderella. However, Cinderella, notwithstanding her mean apparel, was a hundred times handsomer than her sisters, though they were always dressed very richly.

It happened that the King's son gave a ball, and invited all persons of fashion to it. Our young misses were also invited, for they cut a very grand figure among the quality. They were mightily delighted at this invitation, and wonderfully busy in choosing out such gowns, petticoats, and head-clothes as might become them. This was a new trouble to Cinderella; for it was she who ironed her sisters' linen, and plaited their ruffles; they talked all day long of nothing but how they should be dressed.

"For my part," said the eldest, "I will wear my red velvet suit with French trimming."

"And I," said the youngest, "shall have my usual petticoat; but then, to make amends for that, I will put on my gold-flowered manteau, and my diamond stomacher, which is far from being the most ordinary one in the world."
They sent for the best tire-woman they could get to make up their head-dresses and adjust their double pinners, and they had their red brushes and patches from Mademoiselle de la Poche.

Cinderella was likewise called up to them to be consulted in all these matters, for she had excellent notions, and advised them always for the best, nay, and offered her services to dress their heads, which they were very willing she should do. As she was doing this, they said to her:

"Cinderella, would you not be glad to go to the ball?"

"Alas!" said she, "you only jeer me; it is not for such as I am to go thither."
"Thou art in the right of it," replied they; "it would make the people laugh to see a Cinderwench at a ball."

Anyone but Cinderella would have dressed their heads awry, but she was very good, and dressed them perfectly well They were almost two days without eating, so much were they transported with joy. They broke above a dozen laces in trying to be laced up close, that they might have a fine slender shape, and they were continually at their looking-glass. At last the happy day came; they went to Court, and Cinderella followed them with her eyes as long as she could, and when she had lost sight of them, she fell a-crying.

Her godmother, who saw her all in tears, asked her what was the matter.
"I wish I could--I wish I could--"; she was not able to speak the rest, being interrupted by her tears and sobbing.

This godmother of hers, who was a fairy, said to her, "Thou wishest thou couldst go to the ball; is it not so?"
"""

model = BartForConditionalGeneration.from_pretrained("sshleifer/distilbart-cnn-12-6")
tokenizer = BartTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

input_ids = tokenizer.encode(text, return_tensors="pt")
generated_sequence = model.generate(input_ids=input_ids)


output_text = tokenizer.decode(generated_sequence.squeeze(), skip_special_tokens=True)
print(output_text)