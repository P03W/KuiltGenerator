settings_gradle_content = """pluginManagement {
    repositories {
        maven { url = "https://server.bbkr.space/artifactory/libs-release/" }
        maven {
            name = 'Fabric'
            url = 'https://maven.fabricmc.net/'
        }
        gradlePluginPortal()
        maven { url 'https://dl.bintray.com/kotlin/kotlin-eap' }
        mavenCentral()
        maven { url 'https://plugins.gradle.org/m2/' }
    }

    plugins {
        id 'fabric-loom' version loom_version
        id "org.jetbrains.kotlin.jvm" version kotlin_version
    }

}

"""

gitignore = """# gradle
.gradle/
build/
out/

# idea
.idea/
*.iml
*.ipr
*.iws

# fabric
run/
minecraft/
"""
