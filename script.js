function findKeywords() {

    let text = document.getElementById("textInput").value;

    if (text.trim() === "") {
        document.getElementById("result").innerHTML = "⚠ Please enter some text.";
        return;
    }

    text = text.toLowerCase();

    let words = text.match(/\b\w+\b/g);

    let stopWords = [
        "the","is","in","and","to","a","of","for","on","with",
        "as","by","at","an","be","this","that","it","are"
    ];

    let filtered = words.filter(word => !stopWords.includes(word));

    let frequency = {};

    filtered.forEach(word => {
        frequency[word] = (frequency[word] || 0) + 1;
    });

    let sorted = Object.keys(frequency)
        .sort((a,b) => frequency[b] - frequency[a])
        .slice(0,5);

    document.getElementById("result").innerHTML =
        "Top Keywords: <br>" + sorted.join(", ");
}
