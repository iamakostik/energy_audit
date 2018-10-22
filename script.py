import sqlite3

class Database:
    
    def __init__(self):
        self.conn = sqlite3.connect("eaudit.db")
        self.cur = self.conn.cursor()
        self.cur.execute ("CREATE TABLE IF NOT EXISTS audit_appliance (id INTEGER PRIMARY KEY,\
        appliance TEXT,\
        quantity INTEGER, \
        power_rating REAL, \
        duty_cycle REAL, \
        daily_energy REAL, \
        load_profile REAL)")
        self.conn.commit()

    
    def insert(self,appliance, quantity, power_rating, duty_cycle, daily_energy, load_profile):
        self.cur.execute("INSERT INTO audit_appliance VALUES(NULL,?,?,?,?,?,?)",(appliance,quantity,power_rating,duty_cycle,daily_energy,load_profile))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM audit_appliance")
        rows=self.cur.fetchall()
        return rows

    def search(self,appliance):
        self.cur.execute("SELECT * FROM audit_appliance WHERE appliance=?",(appliance,))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM audit_appliance WHERE id=?",(id,))
        self.conn.commit()


    def update(self,id, appliance,quantity, power_rating, duty_cycle, daily_energy, load_profile):
        self.cur.execute("UPDATE audit_appliance SET appliance=?,quantity=?,power_rating=?,duty_cycle=?,daily_energy=?,load_profile=?\
        WHERE id=?", (appliance,quantity,power_rating, duty_cycle, daily_energy, load_profile,id))
        self.conn.commit()

    def total_ed(self):
        self.cur.execute("SELECT SUM(quantity*power_rating*duty_cycle) AS total_ed FROM audit_appliance")
        self.conn.commit()
        total_ed=self.cur.fetchall()
        return total_ed

    def total_tlp(self):
        self.cur.execute("SELECT SUM(quantity*power_rating) AS total_tlp FROM audit_appliance")
        self.conn.commit()
        total_tlp = self.cur.fetchall()
        return total_tlp

    def __del__(self):
        self.conn.close
        
