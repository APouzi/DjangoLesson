# Creating the Pages App - 1:22 When we make a projectapp we have an __init__.py file and it's empty. We don't have to worry about it. Migration's is for any database. Migration's we create we're not going to have any migration's for this particular app, but we will in some of the other ones. Admin is if you want to like you want to show stuff in the admin area. We're not going to need to do that here in our listings app, We will, because we'll want to want to manage our listings from the admin area, but we won't touch this one. And then app.py, this shows you the class of the config. This will actually have to go in our settings file. Models, this is where we create our models. This particular app doesn't have a model, but for instance, "listings" will have like the the the title, the address, the number of bedrooms, all that stuff is going to be defined inside of a model. Then we have our tests if we want to run any tests and a views.py file where we can create methods and we can actually link you URLs to those methods.
#Creating the Pages App - 4:10 we want to go and create the URL file and then go to it (4:10 create a urls.py inside the pages app and go to it)

# Pages Templates & Base Layout - 00:00 You want to go to settings.py to make changes to the Directory so we can allow templates to be used. (:32 go to Settings.py)

# Static Files & Paths - 00:00 We want to handle static files. Then we want to go to the btre_resources folder we downloaded and put in our doc folder. "C:\Users\dimit\Documents\btre_resources\btre_theme\dist\assets". This has all our CSS and such. We want to bring these in as static assets. What we do is we go into the btre_project > btre, and inside the btre folder NOT btre_project folder, we create a directory called "static" and in there we move the whole CSS, JS and Fonts folders but for images we don't want them all(yet), we just want the lightbox and the images there without the folders. We then create a directory in the static called "img" and put all the images in there. (2:23 Now we want to go to our btre/setting.py file, bottom of file)

# Bootstrap Layout Markup - 00:23 So now what I want to do is start to implement our bootstrap theme. So I'm on my base HTML layout, which is in the templates folder and we're going to start adding stuff to this this file from our bootstrap theme. Now, the way that brad does this is with sublime text, which is a different text editor. Brad opens up the bootstrap theme in sublime text. That way I don't get confused by which is which. So I'll know that if it's sublime text, it's just the theme, just the HTML. And our main project is in VST code. So you don't have to do this if you want to open it in the same text editor or something else.( 1:43 go to C:\Users\dimit\Documents\btre_resources\btre_theme\dist and open that folder as workspace folder in notepad++)

# Index, About & Linking - 00:00 We start in the index.html file and we start at the head.. (1:48 go to index.html in notepad++, dist/index.html, then go to index.html and paste them in there.) what I'm going to do is copy everything that we don't have that we didn't put into the base.html. Start above the footer and go all the way up until we are under the navbar. Copy all that and this is going to go and in the index html. 1:01 Now, remember, right now, everything is just static. It's like this form is obviously not going to work. We're not going to get the latest listings. We haven't even installed a database yet. We just want to get the markup to show. And it's going to be like that for quite a while until we get into creating our models and all that stuff. So just keep that in mind. (1:43 go to index.html)