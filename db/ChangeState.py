#!/usr/bin/env python
# coding=utf-8

import sys, getopt
import os
import psycopg2

DATABASE = sys.argv[1]
DBUSER = sys.argv[2]
DBPASSWORD = sys.argv[3]
DBHOST="127.0.0.1"
DBPORT="5432"
ConfigFile="/opt/ericsson/nfvo/fcaps/config/am_collector/application.yml"

CONN = None

def amCollectorHostInfoOperate():
    cur = CONN.cursor()
    cur.execute("SELECT collector_id,node_state,state from am_collector_host_info")
    rows = cur.fetchall()
    for row in rows:
        print("Deal collector_id:", row[0], ",node_state:", row[1], ",state:", row[2])

        if row[1] == 'MASTER':
            cur.execute("update am_collector_host_info set node_state='%s', state='%s' where collector_id='%s'"%('SLAVE','standby',row[0]))
            print("Change node_state to SLAVE, state to standby")
        elif row[1] == 'SLAVE':
            cur.execute("update am_collector_host_info set node_state='%s', state='%s' where collector_id='%s'"%('MASTER','standby',row[0]))
            print("Change node_state to MASTER, state to standby")
        print("Total number of rows operate :", cur.rowcount)

    CONN.commit()
    cur.close()
    CONN.close()
    print("Operation done successfully")

def main():
    global CONN, DBHOST, ConfigFile
    if os.path.exists(ConfigFile):
        with open(ConfigFile, "rb") as f:
            for line in f:
                if line.find('#') == -1 and line.find('jdbc:postgresql') !=-1:
                    DBHOST = line[line.find('sql://')+len('sql://'):line.find(':5432/')]
                    print("DBHOST:",DBHOST)

    CONN = psycopg2.connect(database=DATABASE, user=DBUSER, password=DBPASSWORD, host=DBHOST, port=DBPORT)
    print("Connect database successfully.")

    amCollectorHostInfoOperate()

if __name__ == '__main__':
    main()
