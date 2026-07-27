## 34. Accessibility and Usability

- All map actions must be reachable by keyboard, including tab switching, search, filters, table view, marker-result navigation, details-panel actions and modal controls.
- Do not use marker colour as the only status signal. Pair colour with icon, label, shape or accessible text.
- Status chips, selected cards, table rows and command states must meet the Bolt contrast standard in default, hover, selected, disabled and focus states.
- Provide descriptive accessible names for vehicle markers, clusters, geofences, POIs, map controls and icon-only actions.
- Keyboard focus must remain visible and move predictably when the right panel, filter drawer, action menu or confirmation modal opens.
- Closing a drawer or modal must return focus to the control that opened it.
- Map zoom and pan must not trap keyboard or screen-reader users; an equivalent list or table path must remain available for every operational entity.
- Dynamic live updates should not repeatedly interrupt assistive technology. Announce only meaningful state changes such as a selected vehicle becoming inactive or a command changing status.
- Date, time, distance, speed and number formats should follow the user's locale and organisation settings.
- All timestamps must identify the effective timezone when ambiguity is possible.
- Long names, addresses and translated labels must truncate safely with a tooltip or expandable view; controls must not overlap.

---
