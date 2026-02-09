# Yard & Warehouse Management

#### Dock & Trip Flow

Optimizing turn-around time (TAT) is the primary goal of the Yard module.

* **Trip Purpose:** Every vehicle entering the facility must be assigned a purpose (e.g., Inward Goods, Outbound Dispatch, or Empty movement).
* **Dock Activity:** Track exactly how long a vehicle stays at a specific dock for loading or unloading.
* **Approval Matrix:** Custom workflows where gate-in or gate-out events require digital authorization from a supervisor.

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1).png" alt="Figure 1: Turn-Around Time (TAT) Gauge"><figcaption><p>Turn-Around Time (TAT) Gauge</p></figcaption></figure>

{% hint style="info" %}
The TAT Gauge visualizes the average Gate-to-Gate time.

* Green (0-60 mins): Excellent - Operations are efficient.
* Yellow (60-96 mins): Target - Approaching delay threshold.
* Red (>96 mins): Delayed - Trip requires immediate escalation.
{% endhint %}

#### Guard View & QR Scanning

A simplified, mobile-responsive interface designed for on-site security personnel.

* **Instant Identification:** Guards scan a QR code or IMEI to pull up driver profiles and trip validity.
* **Manual Entry:** Fallback option to search via vehicle registration number if hardware is not yet installed.

#### Security & Guard Operations

* **Guard View:** A simplified, mobile-friendly interface for security guards.
* **QR Scanning:** Use the built-in scanner to quickly check-in vehicles by scanning their dashboard QR code or IMEI.
