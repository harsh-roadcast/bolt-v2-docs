## Checklist and VCR Framework

TripHub should use a generic dynamic form/checklist framework for execution and compliance.

Supported form types:

- VCR Checklists.
- Vehicle Inspection Forms.
- Safety Forms.
- Survey Forms.
- Custom Compliance Forms.

Supported fields:

- Text.
- Paragraph.
- Dropdown.
- Multi-select.
- Checkbox.
- Number.
- Date.
- Image upload.
- File upload.
- Signature.
- Currency.
- URL.

Configuration rules:

- Forms may be route-type level or trip-level.
- Forms may be mandatory before trip start, during target completion or before trip completion.
- No Select All option should be allowed for checklist execution unless the product owner explicitly approves the current mobile design pattern.
- Form responses must be audit logged and exportable.

### Checklist select-all conflict

The pre-trip checklist currently exposes Check All Items and Uncheck All Items, while stricter compliance use cases require individual acknowledgement. Until the product policy is finalised, mandatory safety or VCR checklists should use individual acknowledgement as the safer default.
