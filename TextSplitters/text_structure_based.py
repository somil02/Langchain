# RecursiveCharacterTextSplitter splits text by trying a hierarchy of separators.
#
# By default, it recursively tries the following separators (in order):
# 1. "\n\n"  -> Paragraph break
# 2. "\n"    -> Line break / sentence on a new line
# 3. " "     -> Space (between words)
# 4. ""      -> Character level (last resort)
#
# It first attempts to split using paragraphs. If a chunk is still larger than
# chunk_size, it recursively tries the next separator (line breaks), then spaces,
# and finally individual characters until every chunk satisfies the size limit.
#
# Default separators:
# ["\n\n", "\n", " ", ""]

from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)