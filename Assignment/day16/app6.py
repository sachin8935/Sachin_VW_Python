from flask import Flask, render_template

app = Flask(__name__)

BAD_WORDS = ["dumb", "stupid"]


class CommentProcessor:
    def __init__(self, comments):
        self.comments = comments
        self.flagged_count = 0
        self.most_liked = comments[0]

    def clean_comment(self, text):
        text = text.strip()
        for word in BAD_WORDS:
            text = text.replace(word, "****")
        return text

    def process(self):
        processed = []

        for c in self.comments:
            username = c["username"].upper()
            comment = self.clean_comment(c["comment"])
            likes = c["likes"]
            flagged = c["flagged"]

            tags = []

            if flagged:
                tags.append("Flagged")
                self.flagged_count += 1

            if likes > 100:
                tags.append("Trending")

            if len(comment) > 200:
                tags.append("Long Post")

            if likes > self.most_liked["likes"]:
                self.most_liked = c

            processed.append({
                "username": username,
                "comment": comment,
                "likes": likes,
                "tags": tags,
                "flagged": flagged
            })

        return processed


comments = [
    {"username": "rekha", "comment": "  This project is awesome!  ", "likes": 45, "flagged": False},
    {"username": "rahul", "comment": "This idea is dumb and useless", "likes": 150, "flagged": True},
    {"username": "dharna", "comment": "Great work team. Keep improving!", "likes": 85, "flagged": False},
    {"username": "amit", "comment": "This is a very long comment " * 15, "likes": 210, "flagged": False}
]


@app.route("/")
def home():
    processor = CommentProcessor(comments)
    processed_comments = processor.process()

    all_users = " ".join([c["username"].upper() for c in comments])

    return render_template(
        "index6.html",
        comments=processed_comments,
        total=len(comments),
        flagged=processor.flagged_count,
        most_liked=processor.most_liked["username"].upper(),
        users=all_users
    )


if __name__ == "__main__":
    app.run(debug=True)