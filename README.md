In case this helps someone, here is some code I wrote to convert a JSON array database so that it can be used with the Anki addon "Sentence adder for any language with batch add option" (https://ankiweb.net/shared/info/1682655437).

It converts a JSON array with the sentences stored in the key "jpn" to  a .tsv file following the Tatoeba website's format.

The json array looks like this (downloaded from: https://sentencesearch.neocities.org/ ):
[
  {
    "source": "jlpt-tango/n5",
    "audio_jap": "jlpt-tango/n5/Tango_N5_0001.mp3",
    "jap": "私はアンです。",
    "eng": "I am Anne."
  },
  {
    "source": "jlpt-tango/n5",
    "audio_jap": "jlpt-tango/n5/Tango_N5_0002.mp3",
    "jap": "私はスミスです。",
    "eng": "I am Smith."
  }
]

To use it, simply modify the filenames accordingly and run it.