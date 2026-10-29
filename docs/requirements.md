# Requirements

## 1. Problem

Support teams receive many tickets every day. Someone has to read each ticket, decide which team should handle it and set its priority. Doing this by hand is slow, and urgent tickets can wait in the wrong queue.

## 2. Goal

Build a support ticket system where a machine-learning model reads each new ticket and predicts the right **team** and **priority**. If the model is confident, the ticket goes straight to that team's queue. If it is unsure, a person reviews it first. Agent corrections are saved so the model can be retrained later in a controlled way.

## 3. Users and roles

| Role | What they can do |
|---|---|
| Customer | Register, log in, create tickets, see **only their own** tickets, add comments |
| Support agent | See their team's queue and the review queue, assign tickets, change status, correct team or priority, add comments and internal notes |
| Admin | Everything an agent can do, plus manage users and teams, and see reports |

## 4. Features

### Must have (version 1.0)

- Register and log in; every user has one role
- Role checks on the server for every action
- Create, view, edit and close tickets
- Assign tickets to agents
- Comments on tickets; internal notes visible only to agents and admins
- Search and filter tickets by status, priority, team and assigned agent
- Ticket statuses: `open` → `in_progress` → `resolved` → `closed`
- ML model predicts team and priority for every new ticket
- Confidence-based routing: confident → team queue, unsure → human review queue
- Agent corrections stored for future retraining
- Agent dashboard and admin reports
- Automated tests, run by GitHub Actions on every push
- Browser-based interface

### Nice to have (after version 1.0)

- AI-generated reply drafts using a free AI API
- Email notifications

### Out of scope

- File attachments, live chat, mobile app, payments, non-English tickets

## 5. Main workflows

- **Customer:** log in → create ticket → follow its status → read replies → reply → close
- **Agent:** log in → open team queue or review queue → open a ticket → check the AI suggestion → correct it if wrong → assign → reply → resolve
- **Admin:** log in → view reports → manage users and teams

## 6. Acceptance criteria

| Feature | Done when |
|---|---|
| Create ticket | A logged-in customer submits a subject and description; the ticket is saved with status `open` and a predicted team and priority |
| Privacy | A customer who asks for another customer's ticket gets "not found" |
| Routing | If the model's confidence is below the threshold, the ticket goes to the review queue, not a team queue |
| Corrections | When an agent changes the predicted team or priority, the predicted and corrected values are saved |
| Internal notes | A customer never sees internal notes |
| Role checks | A customer calling an agent-only endpoint gets "forbidden" |

## 7. Data for the model

- Dataset: [`Tobi-Bueck/customer-support-tickets`](https://huggingface.co/datasets/Tobi-Bueck/customer-support-tickets) on Hugging Face, license CC BY-NC 4.0 (non-commercial use)
- It has a team label (`queue`) and a `priority` label, so both predictions are possible
- Known issues to handle: messy label values, duplicate tickets, and probably synthetic (generated) text

## 8. Quality requirements

- **Security:** hashed passwords; secrets only in `.env`, never in Git; role checks on the server
- **Cost:** free tools and free hosting only
- **Testing:** automated tests for every feature
- **Usability:** works on desktop and phone