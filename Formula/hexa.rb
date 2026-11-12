class Hexa < Formula
  desc "Hex editor for the terminal: find bytes, replace, go to, checksums"
  homepage "https://github.com/siriokds/homebrew-tap"
  version "0.2.0"

  depends_on arch: :arm64
  depends_on :macos

  # The program already built: nothing is compiled on install.
  on_macos do
    on_arm do
      url "https://github.com/siriokds/homebrew-tap/releases/download/hexa-#{version}/hexa-#{version}-macos-arm64.tar.gz"
      sha256 "014835a71aede84b58e71baa091a66430063f912a985fbc3a414d07f6ac81f86"
    end
  end

  def install
    bin.install "hexa"
  end

  test do
    assert_match "hexa #{version}", shell_output("#{bin}/hexa --version")
  end
end
