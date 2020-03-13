# Child event journeys

Welcome!

This code was originally developed by [Celine Gross](https://github.com/Cece78) and [Kaj Siebert](https://github.com/kws) at Social Finance as part of a grant funded programme to support Local Authorities to collaborate on data analysis. The programme was called the ‘Front Door Data Collaboration’. It was supported financially by the Christie Foundation and Nesta (through the ‘What Works Centre for Children’s Social Care’). The LAs whose staff guided its development were Bracknell Forest, West Berkshire, Southampton, and Surrey. It also benefitted from advice from the National Performance and Information Managers Group and from the Ofsted Social Care Inspection Insight team.

We are happy to share this code hoping that others may benefit from **a quick way to create children journeys from their Annex A.** 
This code can be used by anyone holding Annex A data. Little Python knowledge is required to run this code.

You can find more information about Social Finance Digital Labs on our website https://www.sfdl.org.uk/ and our blog https://medium.com/social-finance-uk.



## What does this code do?

**What is the child's journey through social care?**

Getting a longitudinal view of the child's journey through social care is not easy with [Annex A](https://www.gov.uk/government/publications/inspecting-local-authority-childrens-services-from-2018). Annex A is a spreadsheet containing different tabs for different "types" of events: List 1 for Contacts, List 2 for Early Help assessments, etc. It contains useful data but it does not allow to get the whole picture of what happened to each child (unless you want to run from one tab to the next, frantically hitting Ctrl+F to find events related to a particular child...).

**That is a problem because understanding the child's experience is key to providing better support**. Analysing events in isolation (e.g. looking only at Contacts, or Referrals) is valuable, but not enough for a comprehensive view.

**This code creates a simple "journey" line showing the experience of the child from the Annex A data**. For each child, you'll be able to read a one-liner in the following format:
```
[2025-03-01/contact] -> [2025-05-02/contact] -> [2025-05-05/referral] -> [2025-05-10/assessment_start]
```
In this example, the child had a first contact on 1 March 2025, followed by a second contact on 2 May 2025. This second contact triggers a referral on 5 May 2025 and an assessment start on 10 May 2025.

We also included a "reduced" journey line to enable you to do quick searches on journey patterns. In its "reduced" form, the above example would be:
```
C -> C -> R -> AS
```
The reduced column allows for easy searches: if I wanted to see all the children who had at least 3 contacts one after the other, I could do a quick Ctrl+F on "C -> C -> C".



## How to run this programme

### Requirements
To run this programme, you will need to:
- Have installed Python and created a conda environment aligned with requirements.txt.
- Have an Annex A spreadsheet aligned with the [Annex A Ofsted guidance](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/824188/Child-level_data_-_additional_guidance_and_template_for_Annex_A__1_.ods). In particular:
    - The input file tabs are labeled "List_1", "List_2", etc.
    - The first row of each tab is the column headers
    - The column names are aligned with the Annex A guidance. If the code cannot find a column, it will output "Can't find the column X" when you run it.


### Running the code
The only code you need to run is in the child_journeys_creation notebook. You'll need to:
- Define the filepath to the input_file: your Annex A
- Define the filepath to the output_file: the output file will be an Excel table with 1) the child unique ID, 2) the child journey, 3) the "reduced" child journey. There will be a second tab explaining the abbreviations in the reduced journey.
- Run all the cells!

At the moment, the code uses the data in ```data/annexa_example.xlsx``` as an example. Feel free to run the code with this mock data to see what the output looks like before changing the filepaths.


### Understanding what is happening in the background
Most of the action is happening in the ```functions``` folder where you'll find some dictionaries and functions.

The steps are:
1. The code runs through your input_file and finds a list of events to pick up (e.g. List 1, column "Date of Contact" = contact) defined in the ```journey_events``` dictionary. 
2. The code creates a flat file of all these events with the ```build_annexarecord``` function.
3. The code groups all the events per child ID and transforms them into a string with the ```create_journeys``` function.



## Assumptions and caveats

- This is a very simple attempt at creating a child journey that is limited to the data contained in Annex A. In no case should it be used to make any conclusions. Rather, it should be a tool to raise questions and investigate further.
- The child journey is only as good as the data. If your Annex A spreadsheet contains erros, the child journey might too.
- We made a decision to include most dates from Lists 1 to 8 in the child journey. Feel free to change what to include in the ```journey_events``` dictionary.



## Contributing

We'd be very happy for you to contribute! Head over to [CONTRIBUTING.md](CONTRIBUTING.md) for more information.
