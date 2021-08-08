//Instructions to execute script :
//mongo localhost:27017 mongodbinit.js

// Current Database name: retailstore in alignment with init.py
db = db.getSiblingDB('retailstore');

//Adding users
db.users.insertOne(
   { "id" : 1,
     "email" : "test@test.com",
	 "username" : "jeo",
	 "description" : "Jeo focuses on these",
	 "code" : "1234",
	 "public_id" : "test@test.com",
     "password_hash" : "$2b$12$awY1rpk27ZFRNrdDE2Fy/ubKLvTku/yOOQjvCg.LvCn8fIT2yU7Z2"
   }
)

//Adding 
db.product_types.insertOne(
   { "id" : 1,
     "name" : "BOOK",
	 "description" : "Includes eBooks and Physical books",
	 "code" : "BKCODE1"
   }
)
db.product_types.insertOne(
   { "id" : 2,
     "name" : "CAMERA",
	 "description" : "All types of Camera",
	 "code" : "CAMERA234"
   }
)

db.product_types.insertOne(
   { "id" : 3,
     "name" : "COMPUTER",
	 "description" : "All Types of Computer",
	 "code" : "COMP456"
   }
)

db.product_types.insertOne(
   { "id" : 4,
     "name" : "COMPUTER ACCESSORIES",
	 "description" : "Mouse, Keyboard etc",
	 "code" : "COMPAC234"
   }
)
//Add Products
db.products.insertOne(
   { "id" : 1,
     "name" : "The Unicorn Project",
	 "description" : "Author: Gene Kim",
	 "producttype_id" : 1,
	 "imagename" : "unicorn_project_book.png"
   }
)

db.products.insertOne(
   { "id" : 2,
     "name" : "CANON SLR",
	 "description" : "Company: CANON, Make: SLR",
	 "producttype_id" : 2,
	 "imagename" : "canon_dslr_camera.png"
   }
)

db.products.insertOne(
   { "id" : 3,
     "name" : "DELL PC 120",
	 "description" : "Company: DELL, Make: 120C",
	 "producttype_id" : 3,
	 "imagename" : "dell_120_pc.png"
   }
)

