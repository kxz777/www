import random
import json
#https://intoli.com/blog/making-chrome-headless-undetectable/
#https://intoli.com/blog/not-possible-to-block-chrome-headless/
def getAll():
    return pluginTest() + webdriveTest() + chromeTest()
    #Ainda não estou utilizando permisionTest() e webGLVendorAndRenderer porque não estão funcionando
    #return chromeTest() + permisionTest() + pluginTest() + webdriveTest() + webGLVendorAndRenderer()

def chromeTest():
    return """
    window.chrome = 
    {
        app: {
            isInstalled: false,
        },
        webstore: {
            onInstallStageChanged: {},
            onDownloadProgress: {},
        },
        runtime: {
            PlatformOs: {
            MAC: 'mac',
            WIN: 'win',
            ANDROID: 'android',
            CROS: 'cros',
            LINUX: 'linux',
            OPENBSD: 'openbsd',
            },
            PlatformArch: {
            ARM: 'arm',
            X86_32: 'x86-32',
            X86_64: 'x86-64',
            },
            PlatformNaclArch: {
            ARM: 'arm',
            X86_32: 'x86-32',
            X86_64: 'x86-64',
            },
            RequestUpdateCheckStatus: {
            THROTTLED: 'throttled',
            NO_UPDATE: 'no_update',
            UPDATE_AVAILABLE: 'update_available',
            },
            OnInstalledReason: {
            INSTALL: 'install',
            UPDATE: 'update',
            CHROME_UPDATE: 'chrome_update',
            SHARED_MODULE_UPDATE: 'shared_module_update',
            },
            OnRestartRequiredReason: {
            APP_UPDATE: 'app_update',
            OS_UPDATE: 'os_update',
            PERIODIC: 'periodic',
            },
        },
    };
    """

def permisionTest():
    return """
        window.navigator.permissions.query = (parameters) => (
            parameters.name === 'notifications' ?
            Promise.resolve({ state: Notification.permission }) :
            window.navigator.permissions.query(parameters)
        );
    """   

def pluginTest():
    plugins = [
        "Dark Reader",
        "CrxMouse Gestures",
        "FlowCrypt",
        "Pablo",
        "Papier",
        "Screencastify",
        "Wikiwand",
        "Session Buddy"
    ]

    lis     = []
    size    = random.randint(1,7)
    for x in range(size):
        lis.append(plugins[x])
    lis = json.dumps(lis)


    return """
        Object.defineProperty(navigator, 'plugins', {
        get: function() {
            return """ + lis + """;
        },
        });"""

def webdriveTest():
    return """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false,
    });
    """

def webGLVendorAndRenderer():
    return"""
    const getParameter = WebGLRenderingContext.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
    // UNMASKED_VENDOR_WEBGL
    if (parameter === 37445) {
        return 'Intel Open Source Technology Center';
    }
    // UNMASKED_RENDERER_WEBGL
    if (parameter === 37446) {
        return 'Mesa DRI Intel(R) Ivybridge Mobile ';
    }

    return getParameter(parameter);
    };    
    """