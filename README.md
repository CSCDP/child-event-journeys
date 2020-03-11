# Child event journeys

Welcome!

This code was originally developed by [Celine Gross](https://github.com/Cece78) and [Kaj Siebert](https://github.com/kws) at Social Finance as part of a grant funded programme to support Local Authorities to collaborate on data analysis. The programme was called the ‘Front Door Data Collaboration’. It was supported financially by the Christie Foundation and Nesta (through the ‘What Works Centre for Children’s Social Care’). The LAs whose staff guided its development were Bracknell Forest, West Berkshire, Southampton, and Surrey. It also benefitted from advice from the National Performance and Information Managers Group and from the Ofsted Social Care Inspection Insight team.

We are happy to share this code hoping that others may benefit from a quick way to draw children journeys from their Annex A.

This code is for data analysts from a Local Authority or from another body holding Annex A data. Little Python knowledge is required to run this code.

You can find more info about Social Finance Digital Labs on our website https://www.sfdl.org.uk/ and our blog https://medium.com/social-finance-uk.



## What does this code do?

**What is the child's journey through social care?**

Getting a longitudinal view of the child's journey through social care is not easy with Annex A. Annex A is a spreadsheet containing different tabs for different "types" of events: List 1 for Contacts, List 2 for Early Help assessments, etc. Although it contains useful data, it does not allow to get the whole picture for each child (unless you want to run from one tab to the next, frantically hitting Ctrl+F to find events related to a particular child...).

**That is a problem because understanding the child's experience is key to providing better support**. Analysing events in isolation (e.g. looking only at Contacts, or Referrals) is valuable, but not enough for a comprehensive view.

**This code creates a simple "journey" line showing the experience of the child within the Annex A data**. For each child, you'll be able to read a simple one-liner in the following format:
```
[2025-03-01/contact] -> [2025-05-02/contact] -> [2025-05-05/referral] -> [2025-05-10/assessment_start]
```

We also included a "reduced" journey line to enable you to do quick searches on journey patterns. You would see the above example in the following format:
```
C -> C -> R -> AS
```


## How to run this programme



## Assumptions and caveats



## Contributing

We'd be very happy for you to contribute! Head over to [CONTRIBUTING.md](CONTRIBUTING.md) for more information.