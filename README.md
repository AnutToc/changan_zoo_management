# CHANGAN Zoo Management System

An easy-to-use Odoo 17 module for managing CHANGAN Zoo. It helps you keep track of your animals, zoo zones, and zookeepers.

## 🌟 Features

### 1. Animals
* **Detailed Info:** Save animal names, groups (like Mammal, Reptile, Bird), species, gender, and pictures.
* **Health Checks:** Track the next health check date. Colors will show if the check is Normal (Green), Upcoming (Yellow), or Overdue (Red).
* **Life Status:** Mark animals as Alive, Sick, Transferred, or Deceased.
* **Auto Age:** Age is calculated automatically from the birth date.

### 2. Zoo Zones
* Organize your zoo into areas like "African Savanna" or "Reptile House".
* Assign a zookeeper to take care of each zone.
* See how many animals live in each zone easily.

### 3. Zookeepers
* Keep records of your staff (name, position, age, picture, and salary).
* See how many zones each zookeeper manages using Smart Buttons.

### 4. Easy to Use (UI/UX)
* **Kanban Cards:** See animals, zones, and zookeepers as nice picture cards. 
* **Smart Buttons:** Click a button to jump from a zookeeper to their zones, or from a zone to its animals.
* **Search & Group:** Easily find animals by status, gender, or animal group.

### 5. History & Notes (Chatter)
* Write notes and schedule tasks under each animal or zookeeper.
* The system keeps a history of important changes automatically.

### 6. Security
* **Zoo Managers:** Can see and do everything (like viewing secret monthly salaries).
* **Zoo Keepers:** Can read and update normal data, but cannot delete records or see salaries.

---

## 🛠️ How to Install

1. Put the `changan_zoo` folder into your Odoo `addons` folder.
2. Restart your Odoo server.
3. Turn on **Developer Mode** in Odoo.
4. Go to the **Apps** menu and click **Update Apps List**.
5. Search for `CHANGAN Zoo Management` and click **Install**.

*Tip: The module comes with demo data (including pictures, animals, and staff)*
