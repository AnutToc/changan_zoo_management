# CHANGAN Zoo Management System

An Odoo 17 custom module designed to streamline the management of zoo operations, specifically tailored for CHANGAN Zoo. This module helps track animals, living zones, and zookeepers efficiently to reduce operational costs and improve resource management.

## 🌟 Key Features

### 1. Comprehensive Data Management
* **Zookeepers:** Manage staff profiles including name, position, age, picture, and monthly salary.
* **Living Zones:** Organize the zoo into distinct areas, assign responsible zookeepers, and track animals residing in each zone.
* **Animals:** Keep detailed records of every animal, including species, name, age, picture, and their assigned living zone.

### 2. Professional UI/UX & Smart Navigation
* **Kanban Views:** Interactive card-based views for Zookeepers, Living Zones, and Animals. 
  * *Bonus:* Drag and drop animal cards between different living zones directly from the Kanban view!
* **Smart Buttons:** Quick access links within form views. Instantly see how many zones a zookeeper manages or how many animals are in a specific zone.
* **Advanced Search & Filters:** Easily group animals by species or zone, filter out adult animals, or group zookeepers by their positions.

### 3. Built-in Communication & Tracking (Chatter)
* Integrated with Odoo's `mail.thread` and `mail.activity.mixin`.
* Users can leave log notes, schedule activities (e.g., "Vet checkup next week"), and track changes automatically.
* Key fields (like name, assigned zone, and salary) are tracked, so any modifications will be recorded in the chatter history.

### 4. Robust Security & Access Rights
* **Role-Based Access Control:** Divides users into `Zoo Keeper` (Standard) and `Zoo Manager` (Admin).
* **Data Privacy:** Sensitive information such as Zookeeper's *Monthly Salary* is only visible to users in the `Zoo Manager` group.
* Managers have full CRUD (Create, Read, Update, Delete) access, while Keepers have restricted rights to prevent accidental data deletion.

### 5. Data Integrity Constraints
* **Age Validation:** Python constraints ensure that the age of animals and zookeepers cannot be negative.
* **Unique Naming:** SQL constraints guarantee that every Living Zone has a unique name to prevent duplicates.

---

## 🛠️ Installation

1. Navigate to your Odoo custom addons directory.
2. Clone this repository or copy the `changan_zoo` folder into your addons path.
   ```bash
   git clone <your-repository-url> changan_zoo
   ```
3. Restart your Odoo service.
4. Log into Odoo, activate **Developer Mode**.
5. Go to **Apps**, click on **Update Apps List**.
6. Search for `CHANGAN Zoo Management` and click **Install**.

*Note: You can check "Load demonstration data" when creating your database to automatically load sample zookeepers, zones, and animals.*

## 📸 Screenshots
*(Add your screenshots here: Kanban views, Form views with Chatter, Smart Buttons, etc.)*

## 📄 License
This module is licensed under the [LGPL-3.0 License](https://www.gnu.org/licenses/lgpl-3.0.html).
