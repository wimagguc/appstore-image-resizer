# Appstore Image Resizer (Python)

Resizes icons and app screenshots to match iTunes and Google Play requirements.

## Settings

Change these in resize.py:

```
inputDir = "in/"
outputDir = "out/"
format = "ICON" # SCREENSHOT or ICON for now
```

The script will resize *all* files in `inputDir` to match the following formats:

* iPhone 3.5 (640, 960)
* iPhone 4.0 (940, 1136)
* iPhone 4.7 (750, 1334)
* iPhone 5.5 (1242, 2208)

...and all app icon formats that are currently listed in XCode.

You can add any number for other screenshot sizes as well.

## Before you run the script: Virtualenv & requirements

```sh
$ virtulenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Run

```sh
$ source venv/bin/activate
$ python resize.py
```

## License

[MIT, do-with-the-code-whatever-you-please License](https://github.com/wimagguc/appstore-image-resizer/blob/master/LICENSE)

## About

Richard Dancsi

- Blog: [wimagguc.com](http://www.wimagguc.com/)
- Github: [github.com/wimagguc](http://github.com/wimagguc/)
- Twitter: [twitter.com/wimagguc](http://twitter.com/wimagguc/)
- Linkedin: [linkedin.com/in/richarddancsi](http://linkedin.com/in/richarddancsi)