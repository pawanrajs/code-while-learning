const franc = require('franc');
const langs = require('langs');
const colors = require('colors');


const snippet = process.argv[2];

if(snippet) {
    let langCode = franc(snippet, {only: langs.codes("3")});
    if (langCode === 'und') {
        console.log("I'm sorry, I do not understand this language. Give me a longer sentence, maybe?".red);
    } else {
        let languageString = langs.where("3", langCode);
        console.log(`Are you speaking ${languageString.name}?`.green);
    }
} else {
    console.log("Please enter a string as a command line argument after node index.js '<your string here>' ".red);
}