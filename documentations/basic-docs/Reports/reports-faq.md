## Reports FAQ

Short answers to the questions that come up most.

### Questions

#### What's the difference between a saved template and a generated report?

A template is a configuration you keep and rerun. A generated report is a file with data in it. Templates don't expire; generated files do.

#### Why can't I select Events?

Something already selected conflicts with it - most likely Incidents or Stop and Idle. Hover the disabled option for the reason, or try the [compatibility explorer](#report-hierarchy-and-compatibility).

#### Why does MVI clear everything else?

MVI must be generated independently. Selecting it drops the limit to one report.

#### How many reports can I combine?

Four, following the hierarchy top-down, one per level. Unless MVI is selected - then one.

#### Can I build a custom report on my phone?

No. Build it on web, save it as a template, and you can run it from mobile from then on.

#### My report is empty. Is it broken?

Almost certainly not. The date range, the vehicle selection or a filter is excluding everything. See [Troubleshooting](#troubleshooting).

#### Why is my Positions report failing?

Positions produces thousands of rows per vehicle per day. Run one vehicle, one day.

#### Does editing a template change reports I already generated?

No. Existing files are snapshots of the configuration as it was when they ran.

#### Can I rename a column?

Yes - give it an alias. The alias appears in the preview, the file, and any scheduled export.

#### Is the grand total on by default?

No. Turn it on if you need a figure across the whole report.

#### My scheduled report never arrived.

Check the schedule isn't paused, check the recipient address, check spam, and check Last run for whether it actually fired.

#### Why does my report data not match the dates I picked?

Timezone. Check which timezone the report or schedule ran in.

#### Can I cancel a report that's generating?

Needs product confirmation - cancellation appears in the interface but its behaviour isn't specified in the supplied material.

#### How long do generated reports stay available?

Until they expire. The exact retention window needs product confirmation.

------------------------------------------------------------------------

