# Contributing

I will accept PRs but please keep the following in mind.

If you are making a frontend display, I do not believe it should be in this repository, you should make it yourself and I will link to it in the README.

Message me on Discord `underscore95` with any questions related to how the JSON data is stored.

Do not edit the generated .md files manually, your changes will be overwritten next time gen_docs is ran.

Please make an issue before working on a PR.

Some things I think would be good to add:
- Better variable handling (especially replacing local variables with their values in the documentation)
- Fixing bugs (e.g. there is a type with name `"` and messed up fields)
- Manual docs (this should be a separate JSON file which allows contributors to manually add additional information such as a description of what a type is used for, example code, etc)
