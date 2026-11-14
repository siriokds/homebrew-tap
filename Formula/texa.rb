class Texa < Formula
  desc "Small text editor for the terminal, in the spirit of nano and vim"
  homepage "https://github.com/siriokds/homebrew-tap"
  version "0.1.7"

  depends_on arch: :arm64
  depends_on :macos

  # The program already built: nothing is compiled on install. The Linux archive
  # will join the macOS one.
  on_macos do
    on_arm do
      url "https://github.com/siriokds/homebrew-tap/releases/download/texa-#{version}/texa-#{version}-macos-arm64.tar.gz"
      sha256 "2f73a2e9be809d02ae7ce0f5715e291a389e28b194b4f9a1edfb242486c7088e"
    end
  end

  def install
    bin.install "texa"
    doc.install "CREDITS.md"
  end

  test do
    assert_match "texa #{version}", shell_output("#{bin}/texa --version")
  end
end
