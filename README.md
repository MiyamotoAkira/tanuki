
# Tanuki

This is a feature toggling application. The idea is to have a rest api system, that can be used to switch on and off features, and use it to modify the behaviour of your application while the application is running.

## Why the name?

Tanuki is a japanese racoon dog. In Japanese folklore Tanukis has shapeshifting capabilities.

## Motivation.

There are quite a few ways of dealing with switches. Most of the ones I know are really config entries and a few well named methods.

But I wanted a centralized version that could work on a SOA, multi-language environment.

The initial idea is based on [hobknob](https://github.com/opentable/hobknob), a feature toggling application created by Opentable.

## Projects

The following are the projects inside the applicaton

### eu.twoormore.tanuki.api

This is the REST api for Tanuki. This is where the meat of the system will be located.

### eu.twoormore.tanuki.ui

This will be the easy way to configure your switches. It is just a frontend for the api.

### Infrastructure

I want to make it easy to deploy the application and all the needed software. Infrastructure will deal with this concern.

## Usage

For testing purposes you can use the vagrant file provided.

## License

MIT License. See the LICENSE file.

## Collaboration

At this point on time I still have to get the clear picture of the path I am going.
