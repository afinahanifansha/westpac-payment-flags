# Safety, ethics and limitations

- Use synthetic data for the demonstration. The repository contains no real accounts or credentials.
- A production version needs explicit consent, least-privilege access and an auditable purpose for each data field.
- Phone address-book access is not part of the concept. No Call Dad/Call Son/Call David action is provided. Any personal conversation happens outside the prototype.
- Optional location can be missing, stale or inaccurate; travel itself is not evidence of fraud.
- Unusual spending is not automatically fraudulent. Allow correction and legitimate explanations.
- Prevent alert fatigue; evaluate false positives, missed risks and disparities across customer groups.
- Calculate financial amounts deterministically; label uncertain forecasts and ground explanation text in evidence.
- Treat merchant/payee descriptions as untrusted data, never model instructions.
- Trusted-person involvement is optional and revocable. Address coercion, compromise, financial abuse and non-response; share only the payment context authorised by the customer.
- A trusted person cannot view balances or move money. Customer acknowledgement cannot override bank security controls.
- Use calm, accessible language and support human escalation.

The prototype does not demonstrate that these production controls have been implemented. Validation targets include alert relevance, explanation correctness, calculation accuracy, task completion and customer comprehension, compared against a simple rules baseline.
