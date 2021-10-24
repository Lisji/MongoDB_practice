import tkinter as tk
import datetime
import tkinter.ttk as ttk
from bson.objectid import ObjectId
import pymongo
from tkinter import messagebox
import pandas as pd             
import matplotlib.pyplot as plt  
import numpy as np


#建立連線
client = pymongo.MongoClient(
"mongodb+srv://B10723059:lisji8380@cluster0.r36j1.mongodb.net/TRY?retryWrites=true&w=majority"
)

#創建名為bookkeep的DB，及record的collection
db = client.bookkeep
mydb = db.record


class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('資料庫II 期末')
        self.root.geometry('600x300')
        
        init1face(self.root)    

class init1face():
    def __init__(self,master):
        
        self.master = master
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()

        header_label = tk.Label(self.face1, text='資料庫記帳APP')
        header_label.grid(row=0, column=0, columnspan= 2)

        add_btn = tk.Button(self.face1, text='開始記帳',command=self.change1)
        add_btn.grid(row=1, column=0, columnspan= 2)

        change_btn = tk.Button(self.face1, text='更改紀錄',command=self.change2)
        change_btn.grid(row=2, column=0, columnspan= 2)

        delete_btn = tk.Button(self.face1, text='刪除紀錄',command=self.change3)
        delete_btn.grid(row=3, column=0, columnspan= 2)

        search_btn = tk.Button(self.face1, text='搜尋紀錄',command=self.change4)
        search_btn.grid(row=4, column=0, columnspan= 2)

        an_btn = tk.Button(self.face1, text='分析帳務',command=self.change5)
        an_btn.grid(row=5, column=0, columnspan= 2)

    def change1(self,):
        self.face1.destroy()
        initface(self.master)      
    def change2(self,):
        self.face1.destroy()
        changeface(self.master)  
    def change3(self,):
        self.face1.destroy()
        deleteface(self.master)  
    def change4(self,):
        self.face1.destroy()
        searchface(self.master)  
    def change5(self,):
        self.face1.destroy()
        anface(self.master)  
          
class initface():
    def __init__(self,master):
        
        self.master = master
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()
    
        header_label = tk.Label(self.face1, text='開始記帳')
        header_label.grid(row=0, column=0, columnspan= 2)

        date_label = tk.Label(self.face1, text='   日期:  ')
        date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(self.face1)
        date = str(datetime.datetime.now())
        self.date_entry.insert(0,date[0:10])
        self.date_entry.grid(row=1, column=1)


        class_label = tk.Label(self.face1, text='   分類:  ')
        class_label.grid(row=2, column=0)
        self.class_entry = ttk.Combobox(self.face1, 
                                    values=[
                                            "飲食", 
                                            "生活用品",
                                            "電話費",
                                            "房租",
                                            "水電瓦斯",
                                            "其他花費",
                                            "薪水",
                                            "其他收入"])

        self.class_entry.grid(row=2, column=1)


        item_label = tk.Label(self.face1, text='   項目:  ')
        item_label.grid(row=3, column=0)
        self.item_entry = tk.Entry(self.face1)
        self.item_entry.grid(row=3, column=1)

        cost_label = tk.Label(self.face1, text='   花費:  ')
        cost_label.grid(row=4, column=0)
        self.cost_entry = tk.Entry(self.face1)
        self.cost_entry.grid(row=4, column=1)

        income_label = tk.Label(self.face1, text='   收入:  ')
        income_label.grid(row=5, column=0)
        self.income_entry = tk.Entry(self.face1)
        self.income_entry.grid(row=5, column=1)

        calculate_btn = tk.Button(self.face1, text='  確定  ',command=self.change2)
        calculate_btn.grid(row=6, column=0, columnspan= 2)

        back_btn = tk.Button(self.face1, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)


    def change2(self,): 

        data = {
        "date" : self.date_entry.get(),
        "class" : self.class_entry.get(),
        "item" : self.item_entry.get(),
        "cost" : int(self.cost_entry.get()),
        "income" : int(self.income_entry.get())
        }
        mydb.insert_one(data)
        messagebox.showinfo("提示", "紀錄成功")
        self.face1.destroy()
        init1face(self.master)
        

    def change1(self,):       
        self.face1.destroy()
        init1face(self.master)  

class changeface():
    def __init__(self,master):
        self.master = master
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='更新頁面')
        header_label.grid(row=0, column=0, columnspan= 2)

        sea_label = tk.Label(self.face2, text='   搜尋日期:  ')
        sea_label.grid(row=3, column=0)
        self.sea_entry = tk.Entry(self.face2)
        self.sea_entry.grid(row=3, column=1)

        calculate_btn = tk.Button(self.face2, text='  確定  ',command=self.change2)
        calculate_btn.grid(row=6, column=0, columnspan= 2)

        back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)

    def change1(self,):       
        self.face2.destroy()
        init1face(self.master)  

    
    def change2(self,):
        info = self.sea_entry.get()      
        self.face2.destroy()
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='搜尋結果')
        header_label.grid(row=0, column=0, columnspan= 2)
        tree = ttk.Treeview(self.face2,columns=['1','2','3','4','5','6'],show='headings')
        tree.column('1',width=1,anchor='center')
        tree.column('2',width=100,anchor='center')
        tree.column('3',width=100,anchor='center')
        tree.column('4',width=100,anchor='center')
        tree.column('5',width=100,anchor='center')
        tree.column('6',width=100,anchor='center')
        tree.heading('1',text='id')
        tree.heading('2',text='日期')
        tree.heading('3',text='分類')
        tree.heading('4',text='項目')
        tree.heading('5',text='花費')
        tree.heading('6',text='收入')
        
        for x in mydb.find({"date":{"$regex":info}}):
            data = list(x.values())
            tree.insert('','end',values=data)

        tree.grid()
        tree.grid(row=1, column=0)

        
        def set_cell_value(event): # 雙擊進入編輯狀態
            for item in tree.selection():
                item_text = tree.item(item, "values")
                id = item_text[0]
                date = item_text[1]
                class_1 = item_text[2]
                item_1 = item_text[3]
                cost = item_text[4]
                income = item_text[5]

            self.face2.destroy()

            self.face2 = tk.Frame(self.master,)
            self.face2.pack()
            
            header_label = tk.Label(self.face2, text='更改頁面')
            header_label.grid(row=0, column=0, columnspan= 2)
            
            self.id_entry = tk.Entry(self.face2)
            self.id_entry.insert(0,id)

            date_label = tk.Label(self.face2, text='   日期:  ')
            date_label.grid(row=1, column=0)
            self.date_entry = tk.Entry(self.face2)
            self.date_entry.insert(0,date)
            self.date_entry.grid(row=1, column=1)

            class_label = tk.Label(self.face2, text='   分類:  ')
            class_label.grid(row=2, column=0)
            self.class_entry = tk.Entry(self.face2)
            self.class_entry.insert(0,class_1)
            self.class_entry.grid(row=2, column=1)

            item_label = tk.Label(self.face2, text='   項目:  ')
            item_label.grid(row=3, column=0)
            self.item_entry = tk.Entry(self.face2)
            self.item_entry.insert(0,item_1)
            self.item_entry.grid(row=3, column=1)

            cost_label = tk.Label(self.face2, text='   花費:  ')
            cost_label.grid(row=4, column=0)
            self.cost_entry = tk.Entry(self.face2)
            self.cost_entry.insert(0,cost)
            self.cost_entry.grid(row=4, column=1)

            income_label = tk.Label(self.face2, text='   收入:  ')
            income_label.grid(row=5, column=0)
            self.income_entry = tk.Entry(self.face2)
            self.income_entry.insert(0,income)
            self.income_entry.grid(row=5, column=1)

            calculate_btn = tk.Button(self.face2, text='  確定  ',command=self.change3)
            calculate_btn.grid(row=6, column=0, columnspan= 2)

            back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
            back_btn.grid(row=7, column=0, columnspan= 2)

            
        tree.bind('<Double-1>', set_cell_value) # 雙擊左鍵進入編輯
        back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)

    def change3(self,):
        id =self.id_entry.get()
        date = self.date_entry.get()
        class_1 = self.class_entry.get()
        item = self.item_entry.get()
        cost = self.cost_entry.get()
        income = self.income_entry.get()
        mydb.update_one({'_id':ObjectId(id)},{'$set':{'date':date,'class':class_1,'item':item,'cost':int(cost),'income':int(income)}})
        messagebox.showinfo("提示", "更新成功")
        self.face2.destroy()
        init1face(self.master)

class deleteface():
    def __init__(self,master):
        self.master = master
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='刪除頁面')
        header_label.grid(row=0, column=0, columnspan= 2)

        sea_label = tk.Label(self.face2, text='   搜尋日期:  ')
        sea_label.grid(row=3, column=0)
        self.sea_entry = tk.Entry(self.face2)
        self.sea_entry.grid(row=3, column=1)

        calculate_btn = tk.Button(self.face2, text='  確定  ',command=self.change2)
        calculate_btn.grid(row=6, column=0, columnspan= 2)

        back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)

    def change1(self,):       
        self.face2.destroy()
        init1face(self.master)  

    
    def change2(self,):
        info = self.sea_entry.get()      
        self.face2.destroy()
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='搜尋結果')
        header_label.grid(row=0, column=0, columnspan= 2)
        tree = ttk.Treeview(self.face2,columns=['1','2','3','4','5','6'],show='headings')
        tree.column('1',width=1,anchor='center')
        tree.column('2',width=100,anchor='center')
        tree.column('3',width=100,anchor='center')
        tree.column('4',width=100,anchor='center')
        tree.column('5',width=100,anchor='center')
        tree.column('6',width=100,anchor='center')
        tree.heading('1',text='id')
        tree.heading('2',text='日期')
        tree.heading('3',text='分類')
        tree.heading('4',text='項目')
        tree.heading('5',text='花費')
        tree.heading('6',text='收入')
        
        for x in mydb.find({"date":{"$regex":info}}):
            data = list(x.values())
            tree.insert('','end',values=data)

        tree.grid()
        tree.grid(row=1, column=0)

        
        def set_cell_value(event): # 雙擊進入編輯狀態
            for item in tree.selection():
                item_text = tree.item(item, "values")
                id = item_text[0]
                date = item_text[1]
                class_1 = item_text[2]
                item_1 = item_text[3]
                cost = item_text[4]
                income = item_text[5]
                
            self.face2.destroy()

            self.face2 = tk.Frame(self.master,)
            self.face2.pack()
            
            header_label = tk.Label(self.face2, text='是否刪除此筆資料？')
            header_label.grid(row=0, column=0, columnspan= 2)
            
            self.id_entry = tk.Entry(self.face2)
            self.id_entry.insert(0,id)

            date_label = tk.Label(self.face2, text='   日期:  ')
            date_label.grid(row=1, column=0)
            self.date_entry = tk.Entry(self.face2)
            self.date_entry.insert(0,date)
            self.date_entry.config(state='disabled')
            self.date_entry.grid(row=1, column=1)

            class_label = tk.Label(self.face2, text='   分類:  ')
            class_label.grid(row=2, column=0)
            self.class_entry = tk.Entry(self.face2)
            self.class_entry.insert(0,class_1)
            self.class_entry.config(state='disabled')
            self.class_entry.grid(row=2, column=1)

            item_label = tk.Label(self.face2, text='   項目:  ')
            item_label.grid(row=3, column=0)
            self.item_entry = tk.Entry(self.face2)
            self.item_entry.insert(0,item_1)
            self.item_entry.config(state='disabled')
            self.item_entry.grid(row=3, column=1)

            cost_label = tk.Label(self.face2, text='   花費:  ')
            cost_label.grid(row=4, column=0)
            self.cost_entry = tk.Entry(self.face2)
            self.cost_entry.insert(0,cost)
            self.cost_entry.config(state='disabled')
            self.cost_entry.grid(row=4, column=1)

            income_label = tk.Label(self.face2, text='   收入:  ')
            income_label.grid(row=5, column=0)
            self.income_entry = tk.Entry(self.face2)
            self.income_entry.insert(0,income)
            self.income_entry.config(state='disabled')
            self.income_entry.grid(row=5, column=1)

            calculate_btn = tk.Button(self.face2, text='  確定  ',command=self.change3)
            calculate_btn.grid(row=6, column=0, columnspan= 2)

            back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
            back_btn.grid(row=7, column=0, columnspan= 2)

            
        tree.bind('<Double-1>', set_cell_value) # 雙擊左鍵進入編輯
        back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)

            
        
    def change3(self,):
        id =self.id_entry.get()

        mydb.delete_one({'_id':ObjectId(id)})
        messagebox.showinfo("提示", "刪除成功")
        self.face2.destroy()
        init1face(self.master)

class searchface():
    def __init__(self,master):
        self.master = master
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='搜尋頁面')
        header_label.grid(row=0, column=0, columnspan= 2)

        sea_label = tk.Label(self.face2, text='   搜尋日期:  ')
        sea_label.grid(row=3, column=0)
        self.sea_entry = tk.Entry(self.face2)
        self.sea_entry.grid(row=3, column=1)

        calculate_btn = tk.Button(self.face2, text='  確定  ',command=self.change2)
        calculate_btn.grid(row=6, column=0, columnspan= 2)

        back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)

    def change1(self,):       
        self.face2.destroy()
        init1face(self.master)  

    
    def change2(self,):
        info = self.sea_entry.get()      
        self.face2.destroy()
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='搜尋結果')
        header_label.grid(row=0, column=0, columnspan= 2)
        tree = ttk.Treeview(self.face2,columns=['1','2','3','4','5'],show='headings')
        tree.column('1',width=100,anchor='center')
        tree.column('2',width=100,anchor='center')
        tree.column('3',width=100,anchor='center')
        tree.column('4',width=100,anchor='center')
        tree.column('5',width=100,anchor='center')
        tree.heading('1',text='日期')
        tree.heading('2',text='分類')
        tree.heading('3',text='項目')
        tree.heading('4',text='花費')
        tree.heading('5',text='收入')
        for x in mydb.find({"date":{"$regex":info}}):
            data = list(x.values())
            data.pop(0)
            tree.insert('','end',values=data)
        tree.grid()
        tree.grid(row=1, column=0)


        back_btn = tk.Button(self.face2, text='回主頁',command=self.change1)
        back_btn.grid(row=7, column=0, columnspan= 2)

class anface():
    def __init__(self,master):
        self.master = master
        self.face2 = tk.Frame(self.master,)
        self.face2.pack()

        header_label = tk.Label(self.face2, text='分析頁面')
        header_label.grid(row=0, column=0, columnspan= 2)

        sea_label = tk.Label(self.face2, text='   搜尋日期:  ')
        sea_label.grid(row=3, column=0)
        self.sea_entry = tk.Entry(self.face2)
        self.sea_entry.grid(row=3, column=1)

        cost_btn = tk.Button(self.face2, text='花費圓餅圖',command=self.change2)
        cost_btn.grid(row=6, column=0, columnspan= 2)

        dcost_btn = tk.Button(self.face2, text='花費長條圖',command=self.change4)
        dcost_btn.grid(row=7, column=0, columnspan= 2)

        income_btn = tk.Button(self.face2, text='收入圓餅圖',command=self.change3)
        income_btn.grid(row=8, column=0, columnspan= 2)

        back_btn = tk.Button(self.face2, text='  回  主  頁  ',command=self.change1)
        back_btn.grid(row=9, column=0, columnspan= 2)

    def change1(self,):       
        self.face2.destroy()
        init1face(self.master)  

    
    def change2(self,):
        data = self.sea_entry.get()
        agg_result= mydb.aggregate(
        [
        {"$match" : {"date":{"$regex":data}}},
        {"$group" : 
            {"_id" : "$class", 
            "total" : {"$sum" : "$cost"}
            }
        }
        ])
        class_1 = []
        size = []
        for i in agg_result:
            if i['total'] > 0:
                class_1.append(i['_id'])
                size.append(i['total'])
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] 
        plt.pie(size, labels = class_1, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()    
    
    def change4(self,):
        data = self.sea_entry.get()
        agg_result= mydb.aggregate(
        [
        {"$match" : {"date":{"$regex":data}}},
        {"$group" : 
            {"_id" : "$date", 
            "total" : {"$sum" : "$cost"}
            }
        }
        ])
        class_1 = []
        size = []
        for i in agg_result:
            if i['total'] > 0:
                class_1.append(i['_id'])
                size.append(i['total'])
        x = np.arange(len(class_1))
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] 
        plt.bar(x, size)
        plt.xticks(x, class_1)
        plt.xlabel('日期')
        plt.ylabel('花費')
        plt.title('日期花費長條圖')
        plt.show()
    def change3(self,):
        data = self.sea_entry.get()
        agg_result= mydb.aggregate(
        [
        {"$match" : {"date":{"$regex":data}}},
        {"$group" : 
            {"_id" : "$item", 
            "total" : {"$sum" : "$income"}
            }
        }
        ])
        class_1 = []
        size = []
        for i in agg_result:
            if i['total'] > 0:
                class_1.append(i['_id'])
                size.append(i['total'])
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] 
        plt.pie(size, labels = class_1, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()


if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()